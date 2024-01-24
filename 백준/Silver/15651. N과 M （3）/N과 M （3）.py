from itertools import product

N, M = map(int, input().split())

list_N = list(i + 1 for i in range(N))
for i in list(product(list_N, repeat = M)):
    print(*i)