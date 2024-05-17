import math

N = int(input())
if N == 1:
    print(0)
else:
    print(math.ceil(N ** 2 / 2))