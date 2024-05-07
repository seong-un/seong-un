K = int(input())

for k in range(K):
    cls, *scores = map(int, input().split())
    print('Class ' + str(k+1))
    scores = sorted(scores)
    largest_gap = 0
    for i in range(cls-1):
        largest_gap = max(largest_gap, scores[i+1] - scores[i])
    print(f'Max {scores[-1]}, Min {scores[0]}, Largest gap {largest_gap}')