from itertools import combinations

L = int(input())
S = list(map(int, input().split()))
S = S + [0, 1001]
n = int(input())

S.sort()
result = 0
for i in range(L+1):
    if S[i] < n < S[i+1]:
        for j in list(combinations(range(S[i]+1, S[i+1]), 2)):
            if j[0] <= n <= j[1]:
                result += 1

print(result)