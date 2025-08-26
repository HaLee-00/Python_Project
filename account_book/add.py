from account_book.load import load_book
from account_book.save import save_book
import datetime


def add_book():
  raw = input("수입/지출 - 금액 - 카테고리 - 설명 순으로 입력 : ")
  try:
    entry_type, amount_str, category, desc = [
        i.strip() for i in raw.split('-', 3)
    ]
  except ValueError:
    print("입력 형식이 잘못되었습니다. 예) 수입 - 50000 - 월급 - 8월 급여")
    return

  amount_str = amount_str.replace(',', '')
  try:
    amount = int(amount_str)
  except ValueError:
    print("금액은 숫자만 입력하세요.")
    return

  data = load_book()
  day = datetime.date.today().isoformat()

  if day not in data:
    data[day] = []

  data[day].append({
      "type": entry_type,
      "amount": amount,
      "category": category,
      "desc": desc
  })

  save_book(data)
