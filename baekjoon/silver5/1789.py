# 1789. 수들의 합. 
# Binary Search. Silver 5
# https://www.acmicpc.net/problem/1789

S = int(input())

N = 1
while True:
    S -= N
    if S < 0:
        break
    else:
        N += 1

print(N-1)