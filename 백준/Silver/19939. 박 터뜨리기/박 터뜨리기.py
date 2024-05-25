N, K = map(int, input().split())

instance = K * (K+1) / 2
if instance > N:
    print(-1)
else:
    if (N - instance) % K == 0:
        print(K-1)
    else:
        print(K)