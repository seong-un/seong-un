from itertools import permutations

A, B = input().split()
B = int(B)
A = list(A)

cases = list(permutations(A, len(A)))
result = 0
for case in cases:
    if case[0] == '0':
        continue
    A = int(''.join(case))
    if A < B:
        result = max(result, A)

if result == 0:
    print(-1)
else:
    print(result)