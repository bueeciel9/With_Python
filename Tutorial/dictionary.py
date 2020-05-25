# 사전(Dictionary) : 키(key)와 값(Value) 한 쌍을 원소로 가지는 자료형
# 일반적으로 반복문을 돌릴때는, key값을 이용해서 key를 인덱스로 해서 값을 가져온다

dict = {}
dict['안녕'] = 'Hello'
dict['기적'] = 'Miracle'
dict['노력'] = 'Effort'
print(dict)
# i는 인덱스, k는 key값
for i, k in enumerate(dict):
    print("[인덱스 : ", i, "] 한글 : ", k, "/ 영어 : ", dict[k])

