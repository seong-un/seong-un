A, B, N = map(int, input().split())

molecule = A%B
result = 0
for n in range(N):
    molecule *= 10
    result = molecule // B
    molecule %= B

print(result)