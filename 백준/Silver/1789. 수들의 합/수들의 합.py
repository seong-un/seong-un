N = int(input())

sm = 0
for i in range(1, 100000):
    sm += i
    if sm > N:
        print(i - 1)
        break
    elif sm == N:
        print(i)
        break