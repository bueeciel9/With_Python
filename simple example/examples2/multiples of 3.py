x=1
sum = 0
while x<=1000:
    x=x+1
    if x%3==0:
        sum = sum+x

print("1부터 1000까지의 자연수 중 3의 배수의 합 : ", sum)