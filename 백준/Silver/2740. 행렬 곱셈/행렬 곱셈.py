N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]
B = list(zip(*B))

matrix = [[0] * K for _ in range(N)]
for n in range(N):
    for k in range(K):
        result = 0
        for m in range(M):
            result += A[n][m] * B[k][m]
        matrix[n][k] = result

for i in matrix:
    print(*i)