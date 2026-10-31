"""
test_models.py - checks that MixCheck keeps answering when a provider goes down.
No real API is called: _ask_once is replaced by a fake that fails on purpose.

    python -m pytest checks -q
"""

import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import models  # noqa: E402


class FakeHTTPError(Exception):
    def __init__(self, status_code):
        super().__init__(f"HTTP {status_code}")
        self.status_code = status_code


@pytest.fixture(autouse=True)
def fresh_state(monkeypatch):
    models._down_until.clear()
    monkeypatch.setattr(models.time, "sleep", lambda seconds: None)
    yield
    models._down_until.clear()


def fake_models(monkeypatch, behaviour):
    """behaviour: model -> list of results to return in order (an Exception is raised)."""
    calls = []

    def fake(model, prompt):
        calls.append(model)
        outcome = behaviour[model].pop(0) if len(behaviour[model]) > 1 else behaviour[model][0]
        if isinstance(outcome, Exception):
            raise outcome
        return outcome

    monkeypatch.setattr(models, "_ask_once", fake)
    return calls


# ---------- What counts as an outage ----------
@pytest.mark.parametrize("status", [401, 403, 408, 429, 500, 502, 503, 504])
def test_outage_statuses(status):
    assert models.is_outage(FakeHTTPError(status))


@pytest.mark.parametrize("status", [400, 404, 422])
def test_our_own_mistakes_are_not_outages(status):
    assert not models.is_outage(FakeHTTPError(status))


def test_timeouts_and_dropped_connections_are_outages():
    assert models.is_outage(TimeoutError())
    assert models.is_outage(ConnectionError())


# ---------- Retries ----------
def test_short_outage_is_retried_on_the_same_model(monkeypatch):
    calls = fake_models(monkeypatch, {"groq": [FakeHTTPError(503), "def f(): pass"]})
    assert models.ask("groq", "p") == "def f(): pass"
    assert calls == ["groq", "groq"]


def test_ask_never_switches_model(monkeypatch):
    """Benchmark results must come from the model they are labelled with."""
    calls = fake_models(monkeypatch, {"groq": [FakeHTTPError(503)], "gemini": ["x"]})
    with pytest.raises(FakeHTTPError):
        models.ask("groq", "p")
    assert set(calls) == {"groq"}
    assert len(calls) == models.ATTEMPTS


def test_bad_request_is_not_retried(monkeypatch):
    calls = fake_models(monkeypatch, {"gemini": [FakeHTTPError(400)]})
    with pytest.raises(FakeHTTPError):
        models.ask("gemini", "p")
    assert calls == ["gemini"]


# ---------- Failover ----------
def test_down_provider_fails_over_to_the_other_provider(monkeypatch):
    fake_models(monkeypatch, {"groq": [FakeHTTPError(503)], "gemini": ["def f(): pass"]})
    answer = models.ask_with_backup("groq", "p")
    assert answer.text == "def f(): pass"
    assert answer.model == "gemini" and answer.asked == "groq" and answer.fell_back
    assert answer.tried[0][0] == "groq"


def test_backup_is_always_a_different_provider():
    for model, backup in models.BACKUP.items():
        assert models.PROVIDER[model] != models.PROVIDER[backup]


def test_healthy_model_answers_itself(monkeypatch):
    fake_models(monkeypatch, {"gemini": ["ok"], "groq": ["unused"]})
    answer = models.ask_with_backup("gemini", "p")
    assert answer.model == "gemini" and not answer.fell_back


def test_failed_provider_is_skipped_for_the_next_request(monkeypatch):
    """Circuit breaker: the second visitor doesn't wait for the same timeouts again."""
    calls = fake_models(monkeypatch, {"groq": [FakeHTTPError(503)], "gemini": ["ok"]})
    models.ask_with_backup("groq", "p")
    calls.clear()
    answer = models.ask_with_backup("groq", "p")
    assert calls == ["gemini"]
    assert answer.fell_back


def test_every_provider_down_raises_a_clear_error(monkeypatch):
    fake_models(monkeypatch, {"groq": [TimeoutError()], "gemini": [FakeHTTPError(500)]})
    with pytest.raises(models.ModelUnavailable) as info:
        models.ask_with_backup("groq", "p")
    assert [m for m, _ in info.value.tried] == ["groq", "gemini"]


def test_mistake_in_request_does_not_fail_over(monkeypatch):
    calls = fake_models(monkeypatch, {"groq": [FakeHTTPError(400)], "gemini": ["ok"]})
    with pytest.raises(FakeHTTPError):
        models.ask_with_backup("groq", "p")
    assert "gemini" not in calls


# ---------- Voice ----------
def test_transcription_falls_back_to_whisper(monkeypatch):
    def gemini_down(*args):
        raise FakeHTTPError(503)

    monkeypatch.setattr(models, "_gemini_transcribe", gemini_down)
    monkeypatch.setattr(models, "_whisper_transcribe", lambda audio, language: "bari code kodu")
    result = models.transcribe(b"audio", language="kanglish")
    assert result.text == "bari code kodu"
    assert result.service == "whisper" and result.fell_back


def test_spoken_function_name_becomes_the_real_name(monkeypatch):
    monkeypatch.setattr(models, "_gemini_transcribe",
                        lambda *args: "ek function likho jiska naam Reverse String ho. sirf code bhejo")
    result = models.transcribe(b"audio", language="hinglish", function_name="reverse_string")
    assert "reverse_string" in result.text and "sirf" in result.text


def test_transcription_instructions_keep_only_words_and_function_name():
    text = models._transcribe_instructions("kanglish", "missing_number")
    assert "Kannada" in text
    assert "'only'" in text
    assert "missing number" in text and "missing_number" in text
