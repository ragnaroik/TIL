# 11034. 캥거루 세마리2
# Bronze 3. 그리디 알고리즘
# https://www.acmicpc.net/problem/11034

# 1번 시행 시, 바깥쪽의 두 캥거루 중 한 마리가 다른 두 캥거루 사이의 정수 좌표로 점프.
# 최대 몇 번 움직일 수 있을까?

# 예시
# 2 3 5 -> 1
# 3 5 9 -> 3

# 2 3 5 의 경우 2에 있는 친구가 4로 이동하는 경우 하나밖에 없음.
# 3 5 9 는 9가 4로 갈 경우 1번이 끝 / 3이 6으로, 5가 7으로, 6이 8으로 가면 총 3번 가능.
# 맥스에 붙어서 하나씩 줄어들어가는 경우가 최대가 될듯 함.

A, B, C = map(int, input().split())

# A, B, C의 좌표 중 A-B / B-C 사이에 더 먼 쪽으로 하나가 이동해야 함.
# 그런데 틀렸다고 나옴. 왜인지 모르겠음.

def cnt_jump(A, B, C):
    cnt = 0
    while A+1 != B or B+1 != C:
        if B-A >= C-B:
            C = B-1
            B, C = C, B
            cnt += 1
        else:
            A = B+1
            A, B = B, A
            cnt += 1                
    return cnt

print(cnt_jump(A, B, C))