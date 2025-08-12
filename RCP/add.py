import datetime

from RCP.save import save_score


#json에 날짜 추가하기
def add_score(scores):
  day = datetime.date.today().isoformat()

  save_score({day: scores})
  
  
