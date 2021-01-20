# 2108. 통계학
# Silver 4. 구현
# https://www.acmicpc.net/problem/2108
# 시간 초과 문제. find_cnt 에서 시간 문제가 발생하는 듯.
# 찾아본 코드는 Collect 기능 사용. 이는 2108_searched에 있음.

n = int(input())
l = []

for _ in range(n):
    a = int(input())
    l.append(a)

l.sort()

number_mean = round(sum(l)/n)

number_median = l[n//2]

def find_cnt(l):
    numbers = list(set(l))
    numbers.sort()
    cnt_list = {}
    for number in numbers:
        cnt_list[number] = l.count(number)
    max_value = max(cnt_list.values())
    flag = False
    answer_onlyone = 0
    for number in numbers:
        if cnt_list[number] == max_value and flag == False:
            flag = True
            answer_onlyone = number
        elif cnt_list[number] == max_value and flag == True:
            answer = number
            return answer
            break
        else:
            continue
    return answer_onlyone

number_cnt = find_cnt(l)

number_range = l[-1] - l[0]

print(number_mean)
print(number_median)
print(number_cnt)
print(number_range)