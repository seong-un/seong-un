n = int(input())

dp = [5] * 50001

for i in range(1, 224):
    dp[i ** 2] = 1

square = 0
for i in range(1, 50001):
    if dp[i] == 1:
        square += 1
        continue
    for j in range(square, square // 2 - 1, -1):
        dp[i] = min(dp[i - j ** 2] + dp[j ** 2], dp[i])

print(dp[n])