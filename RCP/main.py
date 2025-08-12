from RCP.display import display_rcp
from RCP.load import load_score


#실행
def main():

  while True:
    print("\n=== 가위 바위 보 게임 ===")
    print("1. 게임 시작")
    print("2. 순위 보기")
    print("3. 종료")
    choice = input("번호를 선택하세요 :")

    if choice == "1":
      display_rcp()
    elif choice == "2":
      score = load_score()
      if not score:
        print("저장된 점수가 없습니다.")
      else:
        print("\n=== 순위 ===")
        for date, scores in score.items():
          print(
              f"{date} → Player: {scores['player']}점, Computer: {scores['computer']}점"
          )
    elif choice == "3":
      print("게임을 종료합니다.")
      break
    else:
      print("잘못된 입력입니다.")


main()
