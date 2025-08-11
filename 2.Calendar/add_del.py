from save import save_memos


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
