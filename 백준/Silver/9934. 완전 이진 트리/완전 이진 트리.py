from collections import deque

K = int(input())
building = deque(map(int, input().split()))
tree = [[0] * (2 ** i) for i in range(K)]

current = [0, 0]
while current[0] >= 0:
    if current[0] < K - 1:
        if tree[current[0] + 1][2 * current[1]] == 0:
            current = [current[0] + 1, 2 * current[1]]
            continue
        else:
            if tree[current[0]][current[1]] == 0:
                tree[current[0]][current[1]] = building.popleft()
                current = [current[0] + 1, 2 * current[1] + 1]
                continue
            else:
                current = [current[0] - 1, current[1]//2]
    else:
        tree[current[0]][current[1]] = building.popleft()
        current = [current[0] - 1, current[1]//2]

for i in tree:
    print(*i)