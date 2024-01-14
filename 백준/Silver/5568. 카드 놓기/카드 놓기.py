from itertools import permutations

n = int(input())
k = int(input())

integers = []
for i in range(n):
    integers.append(int(input()))

result = set()
for i in list(permutations(integers, k)):
    number = ''
    for j in i:
        number += str(j)
    result.add(int(number))

print(len(result))