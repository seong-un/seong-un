N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

for i in range(N - 1, -1, -1):
    if A[i] == 0:
        M -= 1
        print(B[i], end=" ")
    if M == 0:
        break

for i in range(M):
    print(C[i], end=" ")