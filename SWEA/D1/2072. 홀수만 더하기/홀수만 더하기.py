T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    
    result = 0
    for i in numbers:
        if i % 2 == 1:
            result += i
    print(f'#{test_case} {result}')