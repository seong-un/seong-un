from collections import deque

N = int(input())
A = list(map(int, input().split()))
A.reverse()

queue = deque()
Ai = 1
for i in A:
    if i == 1:
        queue.append(Ai)
    elif i == 2:
        a = queue.pop()
        queue.append(Ai)
        queue.append(a)
    else:
        queue.appendleft(Ai)
    Ai += 1

queue.reverse()
print(*queue)