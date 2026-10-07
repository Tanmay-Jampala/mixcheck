from dotenv import load_dotenv
from google import genai

from grade import grade        # our grader from grade.py

load_dotenv()                 # reads your keys from .env
client = genai.Client()       # uses GEMINI_API_KEY automatically

MODEL = "gemini-flash-lite-latest"
TEST_FILE = "tests/task01.py"

prompts = {
    "english": "Write a Python function named reverse_string that takes a string "
               "and returns it reversed. Reply with only the code.",
    "hinglish": "Ek Python function likho jiska naam reverse_string ho, jo ek string "
                "le aur usko ulta karke return kare. Sirf code bhejna.",
}

for language, prompt in prompts.items():
    response = client.models.generate_content(
        model=MODEL, contents=prompt, config={"temperature": 0}
    )
    print(f"--- {language} ---")
    print(response.text)

    passed, total, error = grade(response.text, TEST_FILE)
    print(f"Score: {passed}/{total} tests passed")
    if error:
        print(f"Error: {error}")
    print()