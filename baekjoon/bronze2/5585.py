# 5585. 거스름돈
# Bronze 2. 그리디 알고리즘
# https://www.acmicpc.net/problem/5585

# 천엔에서 입력된 yen값에 대한 거스름돈을 500엔 / 100엔 / 50엔 / 10엔 / 5엔 / 1엔짜리로 최소개수로 반환하자.

yen = int(input())

def change_yen(yen):
    answer = 0 
    yen = 1000 - yen
    change_unit = [500, 100, 50, 10, 5, 1]
    for unit in change_unit:
        if yen != 0:
            while yen // unit:
                yen -= unit
                answer += 1
        else:
            break
    return answer

print(change_yen(yen))