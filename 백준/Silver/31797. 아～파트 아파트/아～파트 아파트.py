N, M = map(int, input().split())

H = [0] * 10001
for m in range(M):
    floors = map(int, input().split())
    for floor in floors:
        H[floor] = m + 1

alcohol = (N - 1) % (M * 2) + 1
for h in H:
    if h == 0:
        continue
    alcohol -= 1
    if alcohol == 0:
        print(h)
        break