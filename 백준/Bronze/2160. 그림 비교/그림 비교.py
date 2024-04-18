from itertools import combinations

N = int(input())

paints = [[input() for _ in range(5)] for i in range(N)]

min_value = int(1e9)
result = (-1, -1)
for i in list(combinations([_ for _ in range(N)], 2)):
    value = 0
    for a in range(5):
        for b in range(7):
            if paints[i[0]][a][b] != paints[i[1]][a][b]:
                value += 1

    if min_value > value:
        min_value = value
        result = (i[0] + 1, i[1] + 1)

print(*result)