# input() : 사용자로부터 콘솔로 입력을 받는 함수
# int() : 정수 자료형으로 변환
# float() : 문자열, 정수 등의 자료형을 실수형으로 변환
# max(), min() : 시퀀스 자료형에 포함되어 있는 원소 중 최대값 혹은 최소값을 구함
# bin(), hex() : 10진수 ->2진수 변환, 10진수 ->16진수 변환
# round() : 반오림을 수행
# type() : 자료형의 종류


print(round(123.7872879, 3))


print(bin(128))
print(int('0xe6', 16))
list = [5,6,2,6,8,8,9,0]

print(max(list))
print(min(list))

user_input = input('정수를 입력하세요 : ')
print("제곱 : ", int(user_input) ** 2)