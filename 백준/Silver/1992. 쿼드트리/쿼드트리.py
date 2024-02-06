def check(left, right, up, down, result):
    pss = True
    if len(set(''.join(video[up][left:right + 1]))) != 1:
        pss = False
    black_and_white = set()
    for i in range(up, down + 1):
        black_and_white.add(str(video[i][left:right + 1]))
    if len(black_and_white) != 1:
        pss = False
    if pss:
        result += video[up][left]
    else:
        result = compress(left, right, up, down, result)
    return result

def compress(l, r, u, d, result):
    result += '('
    result = check(l, (l+r)//2, u, (u+d)//2, result)
    result = check((l+r)//2 + 1, r, u, (u+d)//2, result)
    result = check(l, (l+r)//2, (u+d)//2 + 1, d, result)
    result = check((l+r)//2 + 1, r, (u+d)//2 + 1, d, result)
    result += ')'
    return result

N = int(input())
video = [list(input()) for i in range(N)]
result = ''
pss = True
if len(set(''.join(video[0]))) != 1:
    pss = False
black_and_white = set()
for i in range(N):
    black_and_white.add(str(video[i]))
if len(black_and_white) != 1:
    pss = False
if pss:
    print(f'{video[0][0]}')
else:
    print(compress(0, N-1, 0, N-1, result))