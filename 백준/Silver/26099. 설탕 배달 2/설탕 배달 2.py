N = int(input())

kg_3 = 0
while N >= 0:
    if N % 5 == 0:
        print(kg_3 + N // 5)
        break
    kg_3 += 1
    N -= 3

if N < 0:
    print(-1)