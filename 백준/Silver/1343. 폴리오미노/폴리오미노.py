board = input().split('.')
answer = ''
for_break = False

for i in board:
    if len(i) % 2 == 1:
        print(-1)
        for_break = True
        break
    else:
        if len(i) % 4 == 0:
            answer += 'A' * len(i)
        else:
            answer += 'A' * (len(i) - 2) + 'BB'
    answer += '.'

if not for_break:
    answer = answer[:len(answer) - 1]
    print(answer)