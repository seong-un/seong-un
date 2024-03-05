N, T, P = map(int, input().split())
P -= 1

participant = [list(map(int, input().split())) for _ in range(N)]

problem = [0] * T
for idx, i in enumerate(list(zip(*participant))):
    problem[idx] = N - sum(i)

P_score = 0
for idx, i in enumerate(participant[P]):
    if i:
        P_score += problem[idx]

result = 1
for idx, i in enumerate(participant):
    if idx == P:
        continue
    score = 0
    for id, j in enumerate(i):
        if j:
            score += problem[id]
    if score > P_score:
        result += 1
    elif score == P_score:
        if sum(participant[idx]) > sum(participant[P]):
            result += 1
        elif sum(participant[idx]) == sum(participant[P]):
            if idx < P:
                result += 1

print(P_score, result)