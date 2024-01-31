N = int(input())
lst = list(map(int, input().split()))

dp = [0 for _ in range(N)]
for i in range(N):
    dp[i] = max(dp[i], 1)
    for j in range(i):
        if lst[j] > lst[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))