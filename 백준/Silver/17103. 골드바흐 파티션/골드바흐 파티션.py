import sys
input = sys.stdin.readline

prime_number = [True] * 1000001
prime_number[0], prime_number[1] = False, False
for i in range(2, 1000001):
    for j in range(i * 2, 1000001, i):
        prime_number[j] = False

T = int(input())
for t in range(T):
    N = int(input())
    result = 0
    for i in range(2, N // 2 + 1):
        if prime_number[i] and prime_number[N - i]:
            result += 1
    print(result)