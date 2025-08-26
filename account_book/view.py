from account_book.load import load_book


#내역 보기
def view_all():
  data = load_book()

  if not data:
    print("저장된 내역이 없습니다.")
    return

  print("\n\t=== 전체 내역 ===")
  for data, entries in data.items():
    print(f"\n{data}")
    for entry in entries:
      print(
          f"  {entry['type']} - {entry['amount']}원 - {entry['category']} - {entry['desc']}"
      )


#특정날짜 내역 보기
def view_day():
  data = load_book()

  day = input("날짜를 입력하세요 : ")

  if day not in data:
    print(f"{day} 날짜에는 저장된 내역이 없습니다")
  else:
    for entry in data[day]:
      print(f"\n{day}")
      print(
          f"  {entry['type']} - {entry['amount']}원 - {entry['category']} - {entry['desc']}"
      )
