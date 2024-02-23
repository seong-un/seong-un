total = 0
scorecard = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0, 'P': 0.0}
sum_credit = 0
for i in range(20):
    subject, credit, grade = input().split()
    total += scorecard[grade] * float(credit)
    if grade != 'P':
        sum_credit += float(credit)

print(total / sum_credit)