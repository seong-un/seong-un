N = int(input())
Pi = list(map(int, input().split()))
Pi = [0] + Pi
dp = [0 for i in range(N+1)]

for i in range(1, N+1):
    for j in range(i, -1, -1):
        dp[i] = max(dp[i], Pi[j] + dp[i - j])

print(dp[-1])