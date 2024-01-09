from collections import deque

N = int(input())
A = list(map(int, input().split()))
A.reverse()

queue = deque()
Ai = 1
for i in A:
    if i == 1:
        queue.appendleft(Ai)
    elif i == 2:
        a = queue.popleft()
        queue.appendleft(Ai)
        queue.appendleft(a)
    else:
        queue.append(Ai)
    Ai += 1

print(*queue)