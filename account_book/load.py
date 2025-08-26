import json
import os


def load_book():
  if not os.path.exists("account.json"):
    return {}

  with open("account.json", "r", encoding="utf-8") as f:
    try:
      return json.load(f)
    except json.JSONDecodeError:
      return {}
