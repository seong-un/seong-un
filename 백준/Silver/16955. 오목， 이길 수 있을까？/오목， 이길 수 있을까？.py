dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

go = [list(input()) for i in range(10)]
for i in range(10):
    for j in range(10):
        if go[i][j] in ['X', 'O']:
            continue
        go[i][j] = 'X'
        for a in range(10):
            for b in range(10):
                if go[a][b] != 'X':
                    continue
                for k in range(8):
                    omok = 1
                    while True:
                        x = a + omok * dx[k]
                        y = b + omok * dy[k]
                        if x < 0 or y < 0 or x >= 10 or y >= 10 or go[x][y] != 'X':
                            break
                        omok += 1
                        if omok == 5:
                            print(1)
                            break
                    if omok == 5:
                        break
                if omok == 5:
                    break
            if omok == 5:
                break
        if omok == 5:
            break
        go[i][j] = '.'
    if omok == 5:
        break
if omok != 5:
    print(0)