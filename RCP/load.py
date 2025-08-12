import json
import os


#json 불러오기
def load_score():

  if not os.path.exists("score.json"):
    return {}

  with open("score.json", "r", encoding="utf-8") as f:
    try:
      return json.load(f)
    except json.JSONDecodeError:
      return {}
