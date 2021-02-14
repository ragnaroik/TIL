# 1259. 팰린드롬수
# Bronze 1. 
# https://www.acmicpc.net/problem/1259

# 거꾸로 읽어도 같은 경우 팰린드롬.
# 맞으면 yes, 아니면 no

def find_palindrome_number(number):
    # number를 str 타입으로 입력받으면 idx 개념을 사용할 수 있다.
    flag = True
    idx = 0
    reverse_idx = -1
    len_of_number = 0
    for _ in number:
        len_of_number += 1
    medium = len_of_number // 2
    while flag:
        if idx != medium:
            if number[idx] != number[reverse_idx]:
                flag = False
            else:
                idx += 1
                reverse_idx -= 1
        else:
            break
    
    if flag:
        return 'yes'
    else:
        return 'no'

import random

while True:
    number = input()
    if number == '0':
        break
    print(find_palindrome_number(number))

# print(find_palindrome_number('111131111'))