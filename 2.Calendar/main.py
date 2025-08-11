from load import load_memos
from display import display_cal
from add_del import add_memos, del_memos


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
      display_cal(year, month, memos)
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
