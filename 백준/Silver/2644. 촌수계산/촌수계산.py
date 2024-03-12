from collections import deque

n = int(input())
kin1, kin2 = map(int, input().split())
m = int(input())

relationship = [[False] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    relationship[a][b] = True
    relationship[b][a] = True

queue = deque()
visited = [False] * (n+1)
queue.append((kin1, 0))
visited[kin1] = True
for_break = False
while queue:
    a, result = queue.popleft()
    if a == kin2:
        print(result)
        for_break = True
        break
    for i in range(n+1):
        if relationship[a][i] and not visited[i]:
            queue.append((i, result + 1))
            visited[i] = True

if not for_break:
    print(-1)