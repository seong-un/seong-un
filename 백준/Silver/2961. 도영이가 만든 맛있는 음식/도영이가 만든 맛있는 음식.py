from itertools import combinations

N = int(input())

taste = [list(map(int, input().split())) for _ in range(N)]

gap = int(1e9)
for i in range(1, N+1):
    for cases in combinations(taste, i):
        sourness = 1
        bitter = 0
        for case in cases:
            sourness *= case[0]
            bitter += case[1]
        gap = min(gap, abs(sourness - bitter))

print(gap)