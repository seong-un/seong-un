N = int(input())

plan = dict()
for n in range(N):
    S, W, D, P = input().split()
    plan[S] = [int(W), int(D), int(P)]

planner = [False] * 70
for n in range(N):
    S, M = input().split()

    if int(M) >= plan[S][2]:
        planner[7 * (plan[S][0]-1) + plan[S][1]] = True

result = 0
continuity = 0
for i in range(70):
    if planner[i]:
        continuity += 1
    else:
        result = max(result, continuity)
        continuity = 0

print(max(result, continuity))