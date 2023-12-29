N, M = map(int, input().split())
S = set()

for i in range(N):
    S.add(input())

answer = 0
for i in range(M):
    if input() in S:
        answer += 1

print(answer)