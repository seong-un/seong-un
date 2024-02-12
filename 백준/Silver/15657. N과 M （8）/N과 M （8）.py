from itertools import combinations_with_replacement

N, M = map(int, input().split())
nature = sorted(list(map(int, input().split())))
cases = list(combinations_with_replacement(nature, M))

for i in cases:
    print(*i)