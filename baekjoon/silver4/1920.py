# 1920. 수 찾기
# Silver 4. 
# https://www.acmicpc.net/problem/1920
# MergeSort 써보려다가 시간이 길어져서 QuickSort 사용해봄.
# sort 방법에 익숙해질 수 있도록 하루에 한 번씩 작성해보려 함.
# binary search도 역시 익숙해지도록 작성해보려함.

import time
import random
# N = 100000
# M = 100000
# list_A = [random.randint(-2**30, 2**30) for _ in range(N)]
# check_list = [random.randint(-2**30, 2**30) for _ in range(M)]

# N = int(input())
# list_A = list(map(int, input().split()))
# M = int(input())
# check_list = list(map(int, input().split()))

start = time.time()

# list_A sort
# def MergeSort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         medium = len(arr) // 2
#         l_arr = arr[:medium]
#         r_arr = arr[medium:]
#         l_arr = MergeSort(l_arr)
#         r_arr = MergeSort(r_arr)
#         return Merge(l_arr, r_arr)

# def Merge(l_arr, r_arr):
#     merged_list = []
#     while len(l_arr) > 0 or len(r_arr) > 0:
#         if len(l_arr) > 0 and len(r_arr) > 0:
#             if l_arr[0] <= r_arr[0]:
#                 merged_list.append(l_arr[0])
#                 l_arr = l_arr[1:]
#             else:
#                 merged_list.append(r_arr[0])
#                 r_arr = r_arr[1:]
#         elif len(l_arr) > 0:
#             merged_list.append(l_arr[0])
#             l_arr = l_arr[1:]
#         elif len(r_arr) > 0:
#             merged_list.append(r_arr[0])
#             r_arr = r_arr[1:]
#     return merged_list

def Merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)
    
    def merge(low, mid, high):
        temp = []
        l, r = low, mid

        while l < mid and r < high:
            if arr[l] < arr[r]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[r])
                r += 1
            
        while l < mid:
            temp.append(arr[l])
            l += 1
        while r < high:
            temp.append(arr[r])
            r += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))

def BinarySearch(arr, number, low, high):
    if not arr:
        return 0
    medium = (low + high) // 2
    if number == arr[medium]:
        return 1
    elif number < arr[medium]:
        return BinarySearch(arr, number, low, medium-1)
    else:
        return BinarySearch(arr, number, medium+1, high)

# list_A = MergeSort(list_A)
# for number in check_list:
    # BinarySearch(list_A, number)
# list_A.sort()
# Merge_sort(list_A)

# quicksort

def Quicksort(arr):
    if len(arr) < 2:
        return arr
    
    low, same, high = [], [], []

    # pivot = arr[random.randint(0, len(arr)-1)]
    pivot = arr[0]
    # pivot = arr[-1]
    # pivot = arr[len(arr)//2]

    for item in arr:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        else:
            high.append(item)

    return Quicksort(low) + same + Quicksort(high)

list_A = Quicksort(list_A)

def Binary(arr, number, start, end):
    if start > end:
        return 0
    medium = (start + end) // 2
    if number == arr[medium]:
        return 1
    elif number < arr[medium]:
        return Binary(arr, number, start, medium-1)
    else:
        return Binary(arr, number, medium+1, end)

for number in check_list:
    Binary(list_A, number, 0, N-1)

print(f'소요시간: {time.time() - start}')