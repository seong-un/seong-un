N = int(input())
scores = [int(input()) for _ in range(N)]

high_level = scores[-1]
result = 0
for i in range(N - 2, -1, -1):
    if scores[i] >= high_level:
        result += scores[i] - high_level + 1
        scores[i] = high_level - 1
    high_level = scores[i]

print(result)