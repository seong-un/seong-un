from itertools import combinations, permutations

N = int(input())

startlink = [list(map(int, input().split())) for i in range(N)]

case_set = set([i for i in range(N)])
min_value = int(1e9)
for case in list(combinations(case_set, N // 2)):
    start, link = 0, 0
    for i in list(permutations(case, 2)):
        start += startlink[i[0]][i[1]]

    for i in list(permutations(case_set - set(case), 2)):
        link += startlink[i[0]][i[1]]

    min_value = min(min_value, abs(start - link))

print(min_value)