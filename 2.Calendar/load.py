import json

#JSON에서 메모 불러오기
def load_memos():
  with open("memos.json", "r", encoding="utf-8") as f:
    try:
      return json.load(f)
    except json.JSONDecodeError:
      return {}