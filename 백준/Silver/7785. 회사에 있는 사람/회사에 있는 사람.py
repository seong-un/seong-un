import sys
input = sys.stdin.readline

n = int(input())

company = set()
for i in range(n):
    person, status = input().split()
    if status == 'enter':
        company.add(person)
    else:
        company.remove(person)

company = sorted(company, reverse=True)

for i in company:
    print(i)