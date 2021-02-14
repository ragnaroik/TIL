# 4641. Doubles
# Bronze 1. 
# https://www.acmicpc.net/problem/4641


# 2~15개의 서로 다른 자연수가 있는 리스트 내에서 정확히 자신의 2배인 수가 있다면 그 개수를 나타내라.

while True:
    arr = list(map(int, input().split()))
    if arr == [-1]:
        break
    else:
        if arr[-1] == 0:
            arr.pop()
        arr.sort()
        cnt = 0
        for i in range(len(arr)):
            find_number = 2 * arr[i]
            for j in range(i+1, len(arr)):
                if find_number == arr[j]:
                    cnt += 1
            
        print(arr)
        print(cnt)
    