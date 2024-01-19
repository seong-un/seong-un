N = int(input())

stair = [[0] * 10 for i in range(101)]
stair[1] = [0] + [1] * 9
for idx, i in enumerate(stair[1:]):
    for jdx, j in enumerate(i):
        if idx < 100 and jdx > 0:
            stair[idx + 1][jdx - 1] += stair[idx][jdx]
        if idx < 100 and jdx < 9:
            stair[idx + 1][jdx + 1] += stair[idx][jdx]

print(sum(stair[N]) % 1000000000)