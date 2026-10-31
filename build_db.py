"""
build_db.py - rebuild mixcheck.db from the prompts, the models' replies and the grades.

Usage:
    python build_db.py

grade_all.py and fix_experiment.py run this for you at the end. The dashboard also builds
the database on its first start if it's missing.
"""

import db

if __name__ == "__main__":
    db.build()
    for table, n in db.counts().items():
        print(f"{table:<10} {n:>5} rows")
    print(f"\nSaved {db.DB_FILE}")
