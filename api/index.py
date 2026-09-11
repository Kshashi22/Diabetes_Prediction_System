import sys
import os

# Make the project root importable so we can pull in the existing app.py
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from app import app  # noqa: E402  (Vercel looks for a variable named `app`)
