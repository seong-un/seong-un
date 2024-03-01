T = int(input())
for t in range(T):
    N = int(input())
    if N == 1:
        print(0)
    else:
        print(int('1' + '2' * (N-2) + '1'))