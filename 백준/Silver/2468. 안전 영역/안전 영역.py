from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())
heights = [list(map(int, input().split())) for i in range(N)]
results = []
for rain in range(0, 101):
    visited = [[False] * N for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if heights[i][j] <= rain or visited[i][j]:
                continue
            result += 1
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            while queue:
                a, b = queue.popleft()
                for k in range(4):
                    x = a + dx[k]
                    y = b + dy[k]
                    if x < 0 or y < 0 or x >= N or y >= N or visited[x][y] or heights[x][y] <= rain:
                        continue
                    queue.append((x, y))
                    visited[x][y] = True
    results.append(result)

print(max(results))