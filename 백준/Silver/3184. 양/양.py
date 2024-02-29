from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

R, C = map(int, input().split())
yard = [input() for _ in range(R)]

visited = [[False] * C for _ in range(R)]
result = [0, 0]
for i in range(R):
    for j in range(C):
        if yard[i][j] == '#' or visited[i][j]:
            continue
        queue = deque()
        queue.append((i, j))
        visited[i][j] = True
        len_v, len_o = 0, 0
        while queue:
            a, b = queue.popleft()
            if yard[a][b] == 'v':
                len_v += 1
            elif yard[a][b] == 'o':
                len_o += 1
            for k in range(4):
                x = a + dx[k]
                y = b + dy[k]
                if x < 0 or y < 0 or x >= R or y >= C or visited[x][y] or yard[x][y] == '#':
                    continue
                queue.append((x, y))
                visited[x][y] = True
        if len_v < len_o:
            result[0] += len_o
        else:
            result[1] += len_v

print(*result)