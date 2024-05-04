import sys
input = sys.stdin.readline

N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]

queue = []
queue.append(((0, 0), (0, 1)))
result = 0
if home[N - 1][N - 1] != 1:
    while queue:
        a, b = queue.pop()
        if a[0] >= N or a[1] >= N or b[0] >= N or b[1] >= N \
                or (home[b[0]][a[1]] + home[a[0]][b[1]] + home[b[0]][b[1]]) >= 1:
            continue
        if b == (N - 1, N - 1):
            result += 1
            continue
        if a[0] == b[0]:
            queue.append(((a[0], a[1] + 1), (b[0], b[1] + 1)))
            queue.append(((a[0], a[1] + 1), (b[0] + 1, b[1] + 1)))
        elif a[1] == b[1]:
            queue.append(((a[0] + 1, a[1]), (b[0] + 1, b[1])))
            queue.append(((a[0] + 1, a[1]), (b[0] + 1, b[1] + 1)))
        else:
            queue.append(((a[0] + 1, a[1] + 1), (b[0] + 1, b[1])))
            queue.append(((a[0] + 1, a[1] + 1), (b[0] + 1, b[1] + 1)))
            queue.append(((a[0] + 1, a[1] + 1), (b[0], b[1] + 1)))

    print(result)
else:
    print(0)