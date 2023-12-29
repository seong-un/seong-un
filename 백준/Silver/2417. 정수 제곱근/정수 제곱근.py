n = int(input())

if n == 0:
    print(0)
else:
    start = 0
    end = 2 ** 63
    while start < end:
        mid = (start + end) // 2
        if mid ** 2 >= n:
            if (mid - 1) ** 2 < n:
                print(mid)
                break
            else:
                end = mid
        else:
            start = mid + 1