# 찾아본 해답

# 2108. 통계학 
# Silver 4. 구현
# https://www.acmicpc.net/problem/2108
# 시간 초과 문제. find_cnt 에서 시간 문제가 발생하는 듯.
# 찾아본 코드는 Collect 기능 사용. 이는 2108_searched에 있음.

import sys 
from collections import Counter

#main
t = int(sys.stdin.readline())

numbers = []
for _ in range(t):
    numbers.append(int(sys.stdin.readline()))
    
def mean(nums):
    return round(sum(nums)/len(nums))

def median(nums):
    nums.sort()
    mid = nums[len(nums)//2] # nums의 개수는 홀수
    
    return mid

def mode(nums):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()    
    
    if len(nums) > 1 : 
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else : 
            mod = modes[0][0]
    else : 
        mod = modes[0][0]

    return mod
        
def scope(nums):
    return max(nums) - min(nums)

print(mean(numbers))
print(median(numbers))
print(mode(numbers))
print(scope(numbers))