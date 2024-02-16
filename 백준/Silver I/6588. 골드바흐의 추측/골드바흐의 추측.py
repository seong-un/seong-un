import sys
input = sys.stdin.readline

prime_number = [True] * 1000001
prime_number[0] = False
prime_number[1] = False
for i in range(2, 1001):
    for j in range(i * 2, 1000001, i):
        prime_number[j] = False

while True:
    n = int(input())

    if n == 0:
        break

    for i in range(3, n//2 + 1, 2):
        if prime_number[i] and prime_number[n - i]:
            print(f'{n} = {i} + {n - i}')
            break