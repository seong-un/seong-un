from collections import deque

N, M = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

campus = [input() for _ in range(N)]

for i in range(N):
    for j in range(M):
        if campus[i][j] == "I":
            queue = deque()
            queue.append((i, j))
            visited = [[False] * M for _ in range(N)]
            visited[i][j] = True
            result = 0
            while queue:
                a, b = queue.popleft()
                for k in range(4):
                    x = a + dx[k]
                    y = b + dy[k]
                    if x < 0 or x >= N or y < 0 or y >= M or visited[x][y] or campus[x][y] == "X":
                        continue
                    if campus[x][y] == 'P':
                        result += 1
                    queue.append((x, y))
                    visited[x][y] = True

if result != 0:
    print(result)
else:
    print("TT")