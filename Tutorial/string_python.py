# 문자열 자료형 뒤집기 : 슬라이싱 활용
# len() : 문자열의 길이를 출력
# isalpha() : 특정한 문자열이 문자로만 이루어져 있는지 확인
# isdigit() : 특정한 문자열이 숫자로만 이루어져 있는지 확인
# isalnum() : 특정한 문자열이 문자와 숫자로만 이루어져 있는지 확인
# join(리스트 자료형) : 여러 개의 문자열을 구분자와 함께 합치는 함수
# sorted(문자열 자료형) : 가 문자를 정렬하는 함수
# split(토큰) : 문자열을 토큰에 따라서 분리하는 함수
# find(서브문자열)  : 문자열 내부에 존재하는 서브 문자열을 찾아주는 함수
# upper(), lower() : 문자열을 대문자 혹은 소문자로 변환하는 함수
# strip() : 좌우로 특정한 문자열을 제거하는 함수
# eval() : 문자열 수식 계산해주는 함수

exp = "(203+705)*3-(30/6)"
print(eval(exp))

str = "   Hello WOrld   "
print(str.strip())

# print(str.upper())
# print(str.lower())

# str = "I like you."
# print(str.find('like'))


# str = "I wanna watch a movie."
# list = str.split(' ')
# print(list)

# list = ['Hello', 'World', '홍길동']
# print('_' .join(list))
# str = "Hello World"
# list = sorted(str)
# print(list)


# print(str[::-1])
# print(len(str))
# print(str.isalpha())
# print(str.isalnum())
