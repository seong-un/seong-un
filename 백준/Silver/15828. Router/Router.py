from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
buffer = deque()
while True:
    packet = int(input())
    if packet == -1:
        if buffer:
            print(*buffer)
        else:
            print("empty")
        break
    elif packet == 0:
        buffer.popleft()
    else:
        if len(buffer) != N:
            buffer.append(packet)