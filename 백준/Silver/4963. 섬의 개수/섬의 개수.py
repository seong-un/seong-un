from collections import deque

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    queue = deque()
    land_sea_map = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    result = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] or land_sea_map[i][j] == 0:
                continue
            result += 1
            queue.append((i, j))
            visited[i][j] = True
            while queue:
                a, b = queue.popleft()
                for k in range(8):
                    x = a + dx[k]
                    y = b + dy[k]
                    if x < 0 or y < 0 or x >= h or y >= w or visited[x][y] or land_sea_map[x][y] == 0:
                        continue
                    queue.append((x, y))
                    visited[x][y] = True

    print(result)