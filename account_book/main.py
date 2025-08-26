from account_book.add import add_book
from account_book.load import load_book
from account_book.view import view_all
from account_book.view import view_day


def main():
  while True:
    print("\n=== 가계부 ===")
    print("1. 수입/지출 추가")
    print("2. 전체 내역 보기")
    print("3. 특정 날짜 내역 보기")
    print("4. 종료")

    choice = input("번호 입력 :")

    if choice == "1":
      add_book()
    elif choice == "2":
      view_all()
    elif choice == "3":
      view_day()
    elif choice == "4":
      print("가계부를 종료합니다.")
      break
    else:
      print("잘못된 입력입니다.")
