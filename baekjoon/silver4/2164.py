# 2164. 카드2
# Silver 4. 브루트포스
# https://www.acmicpc.net/problem/2164

# N = 4인 경우
# 1 1
# 2 2 
# 3 2
# 4 4
# 5 2
# 6 4
# 7 6
# 8 8
# 9 2
# 10 4
# 11 6
# 12 8
# 13 10
# 14 12
# 15 14
# 16 16

# 규칙을 찾아서 풀긴 했지만 왜 이렇게 되는지는 모르겠음.
# 일단 문제대로 하면 card_game은 아래의 함수와 같음.

import time

def card_game(N):
    card_list = [i for i in range(1, N+1)]
    cnt = 0
    while len(card_list) > 1:
        card_list.pop(0)
        card_list.append(card_list.pop(0))
        cnt += 1
        # print(card_list)
    return card_list[0], cnt

N = int(input())

start_time = time.time()

print(card_game(N))



def find_number_2(N):
    range_number = 2
    while N > range_number:
        range_number *= 2
    minus_number = range_number - N
    return N - minus_number

# print(find_number_2(N))
end_time = time.time()
print(end_time-start_time)