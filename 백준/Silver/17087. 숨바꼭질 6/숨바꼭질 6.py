import math

N, S = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    A[i] = abs(A[i] - S)

GCD = A[0]
for i in A:
    GCD = math.gcd(GCD, i)

print(GCD)