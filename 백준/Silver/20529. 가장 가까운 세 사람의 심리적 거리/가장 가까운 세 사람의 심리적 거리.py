from itertools import combinations

T = int(input())
for _ in range(T):
    N = int(input())
    MBTI = list(input().split())

    if len(MBTI) >= 33:
        print(0)
    else:
        min_distance = 1e9
        for mbti in list(combinations(MBTI, 3)):
            distance = 0
            for a, b in list(combinations(mbti, 2)):
                for i in range(4):
                    if a[i] != b[i]:
                        distance += 1
            min_distance = min(min_distance, distance)
        print(min_distance)