N, K = map(int, input().split())

prime_number = [True for _ in range(N+1)]
prime_number[0], prime_number[1] = False, False
for i in range(N+1):
    if not prime_number[i]:
        continue
    else:
        K -= 1
        if K == 0:
            print(i)
            break
        for j in range(i * 2, N + 1, i):
            if prime_number[j]:
                prime_number[j] = False
                K -= 1
            if K == 0:
                print(j)
                break