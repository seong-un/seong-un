N, K = map(int, input().split())

dp = [0 for _ in range(K + 1)]
for i in range(N):
    W, V = map(int, input().split())
    for k in range(len(dp) - 1, -1, -1):
        if dp[k] == 0:
            continue
        try:
            dp[k + W] = max(dp[k] + V, dp[k + W])
        except:
            pass
    try:
        dp[W] = max(V, dp[W])
    except:
        pass

print(max(dp))