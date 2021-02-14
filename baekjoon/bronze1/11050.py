# 11050. 이항 계수 1
# Bronze 1. 
# https://www.acmicpc.net/problem/11050

N, K = map(int, input().split())

# answer = 1

# for i in range(K):
#     answer *= N
#     N -= 1
    
def factorial(number):
    answer = 1
    while number:
        answer *= number
        number -= 1
    return answer

def binomial_coefficient(N, K):
    numerator = factorial(N)
    denominator = factorial(N-K) * factorial(K)
    return numerator // denominator

print(binomial_coefficient(N, K))