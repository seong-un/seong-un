# BFS를 이용한다.
# 먼저 I를 찾고, I에서 출발하여 P를 찾는다.
# X가 나오면 큐에 넣지 않고 진행한다.

from collections import deque

N, M = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

campus = [input() for _ in range(N)]

for i in range(N):
    for j in range(M):
        # 먼저 I를 찾으면 시작
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
            break

if result != 0:
    print(result)
else:
    print("TT")