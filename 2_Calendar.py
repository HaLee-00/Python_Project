import calendar
import json
import os


#JSON에서 메모 불러오기
def load_memos():
  with open("memos.json", "r", encoding="utf-8") as f:
    try:
      return json.load(f)
    except json.JSONDecodeError:
      return {}


#메모를 JSON에 저장
def save_memos(memos):
  with open("memos.json", "w", encoding="utf-8") as f:
    json.dump(memos, f, ensure_ascii=False, indent=2)


#달력 보기
def show_cal(year, month, memos):

  calendar.setfirstweekday(calendar.SUNDAY)
  cal = calendar.monthcalendar(year, month)
  day_width = 3

  title = f"{year}년 {month}월 달력"
  print(title.center(day_width * 7))

  days = ["일", "월", "화", "수", "목", "금", "토"]
  print("".join(i.center(day_width) for i in days))

  for week in cal:
    line = ""
    for day in week:
      if day == 0:
        line += "    "
      else:
        date_key = f"{year}-{month:02d}-{day:02d}"
        if date_key in memos:
          day_str = f"*{day:02d}"
        else:
          day_str = f" {day:02d}"
        line += f"{day_str:>3} "

    print(line)


#메모 추가
def add_memos(memos):
  year, month, day = input("날짜 입력 예)2025-08-09 :").split("-")
  note = input("내용 :")
  memos[f"{year}-{month}-{day}"] = {"내용": note}
  save_memos(memos)
  print("메모 저장 완료!")


#메모 삭제
def del_memos(memos):
  date = input("날짜 입력 예)2025-08-09 :")
  if date in memos:
    del memos[date]
    save_memos(memos)
    print("메모 삭제 완료!")
  else:
    print("해당 날짜에 메모가 없습니다.")


#실행
def main():
  memos = load_memos()

  while True:
    print("\n== 메모 달력 ==")
    print("1. 달력보기")
    print("2. 메모추가")
    print("3. 메모삭제")
    print("5. 종료")
    choice = input("원하는 기능을 선택하세요: ")

    if choice == "1":
      year = int(input("연도 :"))
      month = int(input("월 :"))
      show_cal(year, month, memos)
    elif choice == "2":
      add_memos(memos)
    elif choice == "3":
      del_memos(memos)
    elif choice == "5":
      print("달력을 종료합니다")
      break
    else:
      print("잘못 입력 하였습니다.")


main()
