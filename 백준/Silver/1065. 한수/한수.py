N = int(input())

result = 0
for i in range(1, N + 1):
    X = str(i)
    if len(X) in (1, 2):
        result += 1
        continue
    compare = int(X[0]) - int(X[1])
    result += 1
    for j in range(1, len(X) - 1):
        if int(X[j]) - int(X[j + 1]) == compare:
            continue
        else:
            result -= 1
            break

print(result)