N = int(input())
candidates = [int(input()) for _ in range(N)]

result = 0
while candidates.index(max(candidates)) != 0 or candidates.count(max(candidates)) != 1:
    candidates[candidates[1:].index(max(candidates)) + 1] -= 1
    candidates[0] += 1
    result += 1

print(result)