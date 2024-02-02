from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]

queue = set()
queue.add(((0, 0), board[0][0]))
result = 0
while queue:
    now, alphabet = queue.pop()
    result = max(result, len(alphabet))
    for k in range(4):
        x = now[0] + dx[k]
        y = now[1] + dy[k]
        if x < 0 or x >= R or y < 0 or y >= C or board[x][y] in alphabet:
            continue
        queue.add(((x, y), alphabet + board[x][y]))

print(result)