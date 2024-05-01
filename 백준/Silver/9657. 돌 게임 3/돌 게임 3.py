N = int(input())

game = [None] * 1001
game[1:5] = ['SK', 'CY', 'SK', 'SK']
for i in range(5, 1001):
    if 'CY' in [game[i-1], game[i-3], game[i-4]]:
        game[i] = 'SK'
    else:
        game[i] = 'CY'

print(game[N])