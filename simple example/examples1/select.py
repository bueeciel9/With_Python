prompt = 0
while prompt != 4:
    print("원하는 서비스를 선택하세요\n"
          "1. add\n"
          "2. del\n"
          "3. modify\n"
          "4. quit\n")
    prompt = int(input())
    if prompt == 1:
        print("더할게욤!")
        break
    elif prompt == 2:
        print("뺄게욤!")
        break
    elif prompt == 3:
        print("나눌게욤!")
        break
    elif prompt == 4:
        print("나갈게요~")
    else:
        print("똑바로 넣으세여^^")

print("끝!")
