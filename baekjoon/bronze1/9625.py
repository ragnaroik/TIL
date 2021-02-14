# 9625. BABBA
# Bronze 1. 
# https://www.acmicpc.net/problem/9625

# A -> B -> BA -> BAB -> BABBA -> BABBABAB -> BABBABABBABBA..
# A는 B가 되고, B는 BA가 됨.
# (1,0) (0,1) (1,1) (1,2) (2,3) (3,5)
n = int(input())

AB_arr = [[1,0], [0,1]]

if n <= 2:
    answer_AB = AB_arr[n]
else:
    for i in range(n-1):
        a_cnt = AB_arr[i+1][1]
        b_cnt = AB_arr[i][1] + AB_arr[i+1][1]
        ab_cnt = [a_cnt, b_cnt]
        AB_arr.append(ab_cnt)
    answer_AB = AB_arr[n]
    
for answer in answer_AB:
    print(answer, end=' ')
    