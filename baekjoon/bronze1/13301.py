# 13301. 타일 장식물
# Bronze 1. 동적 프로그래밍
# https://www.acmicpc.net/problem/13301
# 메모리 사용 28776 KB
# 시간 64 ms

# 우선 integer를 입력받은 후 N에 저장.
N = int(input())

def solution(N):
    # 초기값(solution(1)과 solution(2))은 미리 구해둠.
    if N == 1:
        return 4
    elif N == 2:
        return 6
    else:
        # N >= 3일 때
        # 우선 최초로 직전(prev)와 직직전(preprev)의 값 저장
        prev, preprev = 6, 4
        # 
        for i in range(N-2):
            preprev, prev = prev, prev + preprev
        return prev
    
print(solution(N))