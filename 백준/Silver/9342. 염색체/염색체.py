import re

T = int(input())
for _ in range(T):
    chromosome = input()
    condition = re.compile('^[A-F]?A+F+C+[A-F]?$')
    if condition.match(chromosome):
        print('Infected!')
    else:
        print('Good')