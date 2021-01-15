T = int(input())

def find_common_multiple(A,B):
    if A >= B and A % B == 0:
        return A
    elif B > A and B % A == 0:
        return B
    else:
        answer = A * 2
        while answer % B != 0:
            answer += A
        return answer

for _ in range(T):
    A, B = map(int, input().split())
    print(find_common_multiple(A,B))