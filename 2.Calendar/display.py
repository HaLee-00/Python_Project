import json
import calendar


#달력 보기
def display_cal(year, month, memos):

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
