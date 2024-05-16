from itertools import combinations

N, S = map(int, input().split())
integers = list(map(int, input().split()))

result = 0
for N_case in range(1, N + 1):
    for case in list(combinations(integers, N_case)):
        if sum(case) == S:
            result += 1

print(result)