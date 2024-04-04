from collections import deque

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

M, N = map(int, input().split())
banner = [list(map(int, input().split())) for _ in range(M)]

letter = 0
for i in range(M):
    for j in range(N):
        if banner[i][j] == 0:
            continue
        letter += 1
        queue = deque()
        queue.append((i, j))
        banner[i][j] = 0
        while queue:
            a, b = queue.popleft()
            for k in range(8):
                x = a + dx[k]
                y = b + dy[k]
                if x < 0 or y < 0 or x >= M or y >= N or banner[x][y] == 0:
                    continue
                queue.append((x, y))
                banner[x][y] = 0

print(letter)