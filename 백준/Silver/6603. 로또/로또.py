from itertools import combinations

while True:
    k, *lotto = map(int, input().split())
    if not lotto:
        break

    for i in list(combinations(lotto, 6)):
        print(*i)
        
    print()