N = int(input())

dp = [0] * 100001
for i in range(1, 100000):
    dp[i] = int(1e9)
    for j in range(1, int(i ** 0.5 + 1)):
        dp[i] = min(dp[i], 1 + dp[i-j**2])

print(dp[N])