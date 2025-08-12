import json

from RCP.load import load_score

#스코어를 json에 저장
def save_score(scores):
  
  try:
    data = load_score()
  except json.JSONDecodeError:
    data = {}

  data.update(scores)

  with open("score.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)