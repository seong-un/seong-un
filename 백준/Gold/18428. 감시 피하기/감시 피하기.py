from itertools import combinations

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())
corrider = [list(input().split()) for i in range(N)]

list_X = []
for i in range(N):
    for j in range(N):
        if corrider[i][j] == 'X':
            list_X.append((i, j))

for_yes = False
for oo in list(combinations(list_X, 3)):
    encounter = False
    for o in oo:
        corrider[o[0]][o[1]] = 'O'
    for i in range(N):
        for j in range(N):
            if corrider[i][j] != 'T':
                continue

            for k in range(4):
                a = 1
                while True:
                    x = i + dx[k] * a
                    y = j + dy[k] * a
                    if x < 0 or y < 0 or x >= N or y >= N or corrider[x][y] in ['T', 'O']:
                        break
                    if corrider[x][y] == 'S':
                        for o in oo:
                            corrider[o[0]][o[1]] = 'X'
                        encounter = True
                        break
                    a += 1
                if encounter:
                    break
            if encounter:
                break
        if encounter:
            break
    if not encounter:
        print('YES')
        for_yes = True
        break

if not for_yes:
    print('NO')