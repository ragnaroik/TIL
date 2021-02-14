# 2748. 피보나치수(2)
# Bronze 1. 
# https://www.acmicpc.net/problem/2748

n = int(input())

import time
start_time = time.time()

fibonacci_arr = [0, 1]

def fibonacci(n):
    if n < 2:
        return fibonacci_arr[n]
    else:
        for i in range(n-1):
            new_fibonacci_number = fibonacci_arr[i] + fibonacci_arr[i+1]
            fibonacci_arr.append(new_fibonacci_number)
        return fibonacci_arr[n]
print(fibonacci(n))

end_time = time.time()

print(f'소요시간: {end_time - start_time}')