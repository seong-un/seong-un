import sys
input = sys.stdin.readline

N = int(input())

stack = [0] * 1000000
i = 0
for _ in range(N):
    command = list(map(int, input().split()))

    if command[0] == 1:
        stack[i] = command[1]
        i += 1
    elif command[0] == 2:
        if i == 0:
            print(-1)
        else:
            i -= 1
            print(stack[i])
    elif command[0] == 3:
        print(i)
    elif command[0] == 4:
        if i == 0:
            print(1)
        else:
            print(0)
    else:
        if i == 0:
            print(-1)
        else:
            print(stack[i-1])