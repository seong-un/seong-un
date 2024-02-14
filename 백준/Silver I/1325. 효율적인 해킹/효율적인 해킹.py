from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

trust = [[] for i in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split())
    trust[B].append(A)

result = [0 for i in range(N + 1)]
for i in range(1, N + 1):
    queue = deque()
    visited = [False for _ in range(N + 1)]
    queue.append(i)
    visited[i] = True
    while queue:
        a = queue.popleft()
        for k in trust[a]:
            if not visited[k]:
                queue.append(k)
                visited[k] = True
    result[i] = sum(visited)

max_result = 0
answer = []
for idx, i in enumerate(result):
    if max_result < i:
        max_result = i
        answer = [idx]
    elif max_result == i:
        answer.append(idx)

print(*answer)