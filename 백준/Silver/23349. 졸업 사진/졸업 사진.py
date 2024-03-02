N = int(input())
submit = dict()
name_set = set()
for i in range(N):
    name, place, *time = input().split()
    if name not in name_set:
        name_set.add(name)
    else:
        continue
    if place not in submit:
        submit[place] = [0] * 50001
    for i in range(int(time[0]), int(time[1])):
        submit[place][i] += 1

max_key = '~'
max_value = 0
for key, value_list in submit.items():
    for value in value_list:
        if max_value < value:
            max_key = key
            max_value = value
        elif max_value == value:
            l = [max_key, key]
            l.sort()
            max_key = l[0]

result = [max_key, 0, 0]
for idx, i in enumerate(submit[max_key]):
    if i == max_value:
        if result[1] == 0:
            result[1] = idx
    else:
        if result[1] != 0 and result[2] == 0:
            result[2] = idx

print(*result)