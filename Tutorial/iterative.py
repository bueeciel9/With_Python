# 반복문 : 조건에 부합하는 한 특정한 명령어를 반복
# 숫자 범위 표현 : range(시작, 끝)
# continue : continue를 만났을 때 더 이상 명령어를 실행하지 않고
#           다음 반복을 진행한다.
#  break : break를 만나면 반복문을 벗어난다.

sum = 0
for i in range(1,6):
    if i%2==0:
        sum = sum+i
print(sum)