from collections import deque

N, M = map(int, input().split())
dx = [i for i in range(1, 7)]

ladder = []
for i in range(N):
    a, b = map(int, input().split())
    ladder.append((a, b))

snake = []
for i in range(M):
    a, b = map(int, input().split())
    snake.append((a, b))

queue = deque()
queue.append((1, 0))
visited = [False] * 101
visited[1] = True
while True:
    a, n = queue.popleft()
    if a == 100:
        print(n)
        break
    for i in dx:
        x = a + i
        if x > 100 or visited[x]:
            continue
        for_ladder = False
        for j in ladder:
            if j[0] == x:
                queue.append((j[1], n + 1))
                visited[j[1]] = True
                visited[j[0]] = True
                for_ladder = True
                break

        for_snake = False
        for j in snake:
            if j[0] == x:
                queue.append((j[1], n + 1))
                visited[j[1]] = True
                visited[j[0]] = True
                for_snake = True
                break

        if not (for_ladder or for_snake):
            queue.append((x, n + 1))
        visited[x] = True