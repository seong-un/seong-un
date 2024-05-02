import sys
input = sys.stdin.readline

N = int(input())

stack = []
for i in range(N):
    command = input().split()

    if command[0] == '1':
        stack.append(command[1])
    elif command[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == '3':
        print(len(stack))
    elif command[0] == '4':
        if stack == []:
            print(1)
        else:
            print(0)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)