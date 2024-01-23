from collections import deque

dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

T = int(input())
for t in range(T):
    I = int(input())
    current = tuple(map(int, input().split()))
    future = tuple(map(int, input().split()))
    queue = deque()
    turn = 0
    queue.append((current, turn))
    visited = [[False] * I for _ in range(I)]
    visited[current[0]][current[1]] = True
    while True:
        (a, b), turn = queue.popleft()
        if (a, b) == future:
            print(turn)
            break
        for k in range(8):
            x = dx[k] + a
            y = dy[k] + b
            if x < 0 or y < 0 or x >= I or y >= I or visited[x][y]:
                continue
            queue.append(((x, y), turn + 1))
            visited[x][y] = True