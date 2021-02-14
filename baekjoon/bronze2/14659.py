# 14659. 한조서열정리하고옴ㅋㅋ
# Bronze 2. 그리디 알고리즘
# https://www.acmicpc.net/problem/14659

# N개의 arr. 오른쪽으로 자신보다 작은 숫자의 개수가 최대인 경우의 값을 출력.
# 예시
# N = 7
# arr = [6, 4, 10, 2, 5, 7, 11]
# arr[2]인 10이 오른쪽으로 2, 5, 7을 이길 수 있으므로 답은 3.


N = int(input())
peaks_heights = list(map(int, input().split()))

max_kills = 0
temp_kills = 0
hanzo = peaks_heights[0]
for i in range(1, N):
    if hanzo > peaks_heights[i]:
        temp_kills += 1
        if temp_kills > max_kills:
            max_kills = temp_kills
    else:
        hanzo = peaks_heights[i]
        temp_kills = 0
print(max_kills)