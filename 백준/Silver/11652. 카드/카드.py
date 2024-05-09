import sys
input = sys.stdin.readline

N = int(input())
cards = dict()
for n in range(N):
    card = int(input())
    if card in cards:
        cards[card] += 1
    else:
        cards[card] = 1

max_num = 0
result = 0
sorted_key = sorted(cards.keys())
for card in sorted_key:
    if max_num < cards[card]:
        max_num = cards[card]
        result = card

print(result)