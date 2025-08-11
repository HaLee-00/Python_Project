import random

choices = ["가위", "바위", "보"]
score = {'Player': 0, 'Computer': 0}

while True:
  player = input("가위, 바위, 보 중에 하나를 입력하세요 : ")

  if player == "종료":
    print("게임을 종료합니다.")
    print(f"최종 스코어 : Player {score['Player']}점, Computer {score['Computer']}점")
    if score['Player'] > score['Computer']:
      print("Player가 이겼습니다.")
      break
    elif score['Player'] < score['Computer']:
      print("Computer가 이겼습니다.")
      break
    else:
      print("비겼습니다.")
      break

  elif player not in choices:
    print("잘못된 입력입니다. 다시 입력하세요")
    continue

  computer = random.choice(choices)
  print(f"컴퓨터는 {computer}를 선택했습니다.")

  if player == computer:
    print("비겼습니다")
  elif (player == "가위" and computer == "보") or\
       (player == "바위" and computer == "가위") or\
       (player == "보" and computer == "바위"):
    print("이겼습니다")
    score['Player'] += 1
  else:
    print("졌습니다.")
    score['Computer'] += 1

print()
