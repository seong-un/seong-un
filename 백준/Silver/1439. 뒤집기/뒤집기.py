import math

S = input()

current = S[0]
result = 0
for s in S:
    if current != s:
        result += 1
        current = s

print(math.ceil(result/2))