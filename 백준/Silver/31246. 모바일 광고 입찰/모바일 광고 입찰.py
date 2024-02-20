import sys
input = sys.stdin.readline

N, K = map(int, input().split())

AB = []
for i in range(N):
    A, B = map(int, input().split())
    AB.append(B - A)

AB.sort()
if AB[K - 1] < 0:
    print(0)
else:
    print(AB[K - 1])