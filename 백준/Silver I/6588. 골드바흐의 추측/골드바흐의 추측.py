import sys
input = sys.stdin.readline

prime_number = [True] * 1000001
prime_number[0] = False
prime_number[1] = False
for i in range(2, 1001):
    a = 2
    while True:
        try:
            prime_number[i * a] = False
            a += 1
        except:
            break

while True:
    n = int(input())

    if n == 0:
        break

    for idx, i in enumerate(prime_number):
        if not i:
            continue
        if prime_number[n - idx]:
            print(f'{n} = {idx} + {n - idx}')
            break