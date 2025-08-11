import json

#메모를 JSON에 저장
def save_memos(memos):
  with open("memos.json", "w", encoding="utf-8") as f:
    json.dump(memos, f, ensure_ascii=False, indent=2)
