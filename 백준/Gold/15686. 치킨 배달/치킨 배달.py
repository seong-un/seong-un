from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken_house = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken_house.append((i, j))

answer = int(1e9)
for chs in combinations(chicken_house, M):
    closure = set(chicken_house) - set(chs)
    for cch in closure:
        city[cch[0]][cch[1]] = 0

    result = 0
    for h in house:
        ch_result = int(1e9)
        for ch in chs:
            ch_result = min(abs(ch[0] - h[0]) + abs(ch[1] - h[1]), ch_result)
        result += ch_result

    answer = min(result, answer)

    for cch in closure:
        city[cch[0]][cch[1]] = 2

print(answer)