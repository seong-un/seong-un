from collections import deque

T = int(input())
for t in range(T):
    keylogger1 = deque()
    keylogger2 = deque()
    for i in input():
        if i.isalpha() or i.isdigit():
            keylogger1.append(i)
        elif i == '<':
            try:
                keylogger2.appendleft(keylogger1.pop())
            except:
                pass
        elif i == '>':
            try:
                keylogger1.append(keylogger2.popleft())
            except:
                pass
        else:
            try:
                keylogger1.pop()
            except:
                pass

    print(*keylogger1, *keylogger2, sep='')