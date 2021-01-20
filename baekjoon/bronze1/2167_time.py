# 2167. 2차원 배열의 합
# Bronze 1. 구현
# https://www.acmicpc.net/problem/2167
# 시간초과

N, M = map(int, input().split())

overall_list = []

for _ in range(N):
    temp_list = list(map(int, input().split()))
    overall_list.append(temp_list)

K = int(input())
answer_list = []
for _ in range(K):
    i, j, x, y = map(int, input().split())
    i, j, x, y = i-1, j-1, x-1, y-1
    sliced_list = [row[j:y+1] for row in overall_list[i:x+1]]
    sum_value = 0
    for list in sliced_list:
        sum_value += sum(list)
    answer_list.append(sum_value)

for answer in answer_list:
    print(answer)
        