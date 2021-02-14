# 11650. 좌표 정렬하기
# Silver 5. 
# https://www.acmicpc.net/problem/11650

N = int(input())

location_list = []

for _ in range(N):
    location = list(map(int, input().split()))
    location_list.append(location)

location_list.sort(key = lambda loc: (loc[0], loc[1]))

for location in location_list:
    print(location)