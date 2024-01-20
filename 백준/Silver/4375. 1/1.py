while True:
    try:
        result = 1
        n = int(input())
        while True:
            if result % n == 0:
                print(len(str(result)))
                break
            result *= 10
            result += 1
    except:
        break