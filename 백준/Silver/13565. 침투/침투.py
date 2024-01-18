from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

grid = [list(input()) for i in range(M)]

queue = deque()
for idx, i in enumerate(grid[0]):
    if i == '0':
        queue.append((0, idx))
        grid[0][idx] = '2'

result = 'NO'
while queue:
    a, b = queue.popleft()
    if a == M - 1:
        result = 'YES'
        break
    for k in range(4):
        x = a + dx[k]
        y = b + dy[k]
        if x < 0 or y < 0 or x >= M or y >= N or grid[x][y] in ['1', '2']:
            continue
        queue.append((x, y))
        grid[x][y] = '2'

print(result)