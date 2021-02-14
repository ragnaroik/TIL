# 1145. 적어도 대부분의 배수
# Silver 5. 브루트포스
# https://www.acmicpc.net/problem/1145


number_arr = list(map(int, input().split()))

# 세 개의 숫자를 입력받을 때 최소공배수를 구하는 함수
def find_min_common_multiple(a, b, c):
    multiply_number = 1
    while True:
        answer = a * multiply_number
        if answer % b or answer % c:
            multiply_number += 1
        else:
            return answer

# 다섯 개의 숫자 중 세 개를 순서대로 뽑아서 10개의 작은 리스트로 만들기
def seperate_5_to_3(arr):
    seperated_arr = []
    for i in range(5):
        for j in range(i+1, 5):
            for k in range(j+1, 5):
                append_arr = (number_arr[i], number_arr[j], number_arr[k])
                seperated_arr.append(append_arr)
    return seperated_arr

arr = seperate_5_to_3(number_arr)

answer = find_min_common_multiple(number_arr[0], number_arr[1], number_arr[2])
for numbers in arr:
    a, b, c = numbers
    if find_min_common_multiple(a, b, c) < answer:
        answer = find_min_common_multiple(a, b, c)

print(answer)