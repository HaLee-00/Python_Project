import random
import time
from RCP.add import add_score


def display_rcp():
  scores = {"player": 0, "computer": 0}

  while True:
    choices = ["가위", "바위", "보"]

    player = input("가위 바위 보 중에 선택하세요. (저장 선택시 이전화면):")

    if player.strip() == "저장":
      add_score(scores)
      break
    elif player not in choices:
      print("\n잘못입력하였습니다.\n")
      continue
    computer = random.choice(choices)

    print("\n안내면 진거~\n")
    time.sleep(1)
    print("가위~ 바위~ 보!\n")
    time.sleep(1)

    print("player  V  computer")
    print(f" {player}   S    {computer}\n ")

    if player == computer:
      print("비겼습니다. 다시!")
    elif (player == "가위" and computer == "보") or (
        player == "바위" and computer == "가위") or (player == "보"
                                                 and computer == "바위"):
      print("player 승!")
      scores["player"] += 1
    else:
      print("player 패!")
      scores["computer"] += 1

    print(f"\nPlayer : {scores['player']}점\nComputer : {scores['computer']}점")
