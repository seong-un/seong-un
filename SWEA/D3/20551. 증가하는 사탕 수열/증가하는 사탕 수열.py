T = int(input())
for test_case in range(1, T + 1):
    boxes = list(map(int, input().split()))
    
    result = 0
    for i in range(len(boxes) - 2, -1, -1):
        if boxes[i] >= boxes[i + 1]:
            result += boxes[i] - boxes[i + 1] + 1
            boxes[i] = boxes[i + 1] - 1
            if boxes[i] <= 0:
                result = -1
                break
    print(f'#{test_case} {result}')