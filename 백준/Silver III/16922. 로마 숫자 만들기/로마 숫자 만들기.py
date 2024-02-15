from itertools import combinations_with_replacement

N = int(input())

roma = [1, 5, 10, 50]
result = set()
for i in list(combinations_with_replacement(roma, N)):
    result.add(sum(i))

print(len(result))