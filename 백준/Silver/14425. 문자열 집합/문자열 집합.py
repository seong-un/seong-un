N, M = map(int, input().split())
S = []

for i in range(N):
    S.append(input())

answer = 0
for i in range(M):
    if input() in S:
        answer += 1

print(answer)