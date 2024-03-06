from collections import deque

N = int(input())

candy = [list(input()) for _ in range(N)]

def brute():
    value = 0
    result = 0
    for s in range(N):
        for k in range(N):
            if k == 0:
                value = 1
                continue
            else:
                if candy[s][k-1] == candy[s][k]:
                    value += 1
                else:
                    result = max(result, value)
                    value = 1
        result = max(result, value)
    for k in range(N):
        for s in range(N):
            if s == 0:
                value = 1
                continue
            else:
                if candy[s-1][k] == candy[s][k]:
                    value += 1
                else:
                    result = max(result, value)
                    value = 1
        result = max(result, value)
    return result

result = 0
for i in range(N):
    for j in range(N):
        if i != 0 and candy[i][j] != candy[i-1][j]:
            candy[i][j], candy[i-1][j] = candy[i-1][j], candy[i][j]
            result = max(result, brute())
            candy[i][j], candy[i-1][j] = candy[i-1][j], candy[i][j]
        if j != 0 and candy[i][j] != candy[i][j-1]:
            candy[i][j], candy[i][j-1] = candy[i][j-1], candy[i][j]
            result = max(result, brute())
            candy[i][j], candy[i][j-1] = candy[i][j-1], candy[i][j]

print(result)