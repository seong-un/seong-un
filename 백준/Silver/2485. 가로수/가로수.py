import math

N = int(input())

trees = [0] * N
for i in range(N):
    trees[i] = int(input())

numbers = [0] * (N - 1)
for i in range(N - 1):
    numbers[i] = trees[i + 1] - trees[i]

gcd = numbers[0]
for i in range(N - 1):
    gcd = math.gcd(gcd, numbers[i])

print((max(trees) - min(trees)) // gcd - len(numbers))