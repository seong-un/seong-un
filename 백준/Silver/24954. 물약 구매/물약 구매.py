import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
Ci = list(map(int, input().split()))

sale = [[] for _ in range(N)]
for i in range(N):
    pi = int(input())
    for p in range(pi):
        sales = list(map(int, input().split()))
        sale[i].append(sales)

min_price = int(1e9)
for case in list(permutations(range(N), N)):
    price = 0
    ci = Ci[:]
    for i in case:
        price += ci[i]
        if price >= min_price:
            price = int(1e9)
            break
        for j in sale[i]:
            ci[j[0] - 1] = max(1, ci[j[0] - 1] - j[1])
    min_price = min(min_price, price)

print(min_price)