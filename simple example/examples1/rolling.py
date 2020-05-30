# dice rolling
import random

Sum = 0

times = int(input("반복하고싶은 횟수를 입력하세요"))

for x in range(0, times):
    number = random.randint(1, 6)
    Sum += number
    print(x, "번째 숫자 : ", number)
average = Sum / times
print("total average is : ", '%.2f' % average)

if 3.5 < average:
    print("평균 이상입니다!")
else:
    print("평균 이하입니다!")
