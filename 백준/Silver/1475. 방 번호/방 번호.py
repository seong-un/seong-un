N = input()

numbers = [0] * 10

for i in N:
    i = int(i)
    if i == 6 or i == 9:
        if numbers[6] > numbers[9]:
            numbers[9] += 1
        else:
            numbers[6] += 1
    else:
        numbers[i] += 1

print(max(numbers))