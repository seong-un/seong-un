scenario = 0
while True:
    scenario += 1
    n = int(input())

    if n == 0:
        break

    student = []
    for i in range(n):
        student.append(input())

    confiscation = []
    for i in range(2 * n - 1):
        number, alphabet = input().split()
        number = int(number)
        if student[number-1] not in confiscation:
            confiscation.append(student[number-1])
        else:
            confiscation.remove(student[number-1])

    print(scenario, confiscation[0])