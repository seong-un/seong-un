N = int(input())

extension = dict()
for i in range(N):
    file = input().split('.')
    if file[-1] in extension:
        extension[file[-1]] += 1
    else:
        extension[file[-1]] = 1

for i in sorted(extension):
    print(i, extension[i])