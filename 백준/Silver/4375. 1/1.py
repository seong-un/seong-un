# 원래는 나머지를 먼저 구하고 곱하나, 곱하고 나머지를 구하나 같은 값을
# 가지는 성질을 이용하여 구한다. -> 이렇게 구할 경우 시간을 굉장히 줄일 수 있다.
# 그러나 나는 바보라서 그냥 브루트포스 알고리즘을 사용하여 모든
# 1111.. 들을 비교하였다.

while True:
    # 테스트 케이스의 수가 정해져 있지 않거나
    # 테스트 케이스의 정지 신호가 없을 경우 try except 문으로 처리한다.
    try:
        result = 1 # 나누어 떨어지는 수를 찾기 위한 수
        n = int(input())
        
        # 나누어 떨어지는 숫자가 나올 때까지 계속 한다.
        while True:
            if result % n == 0:
                print(len(str(result)))
                break
            result = result * 10 + 1
    except:
        break