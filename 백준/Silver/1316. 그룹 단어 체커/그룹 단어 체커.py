N = int(input())

group_word = 0
for i in range(N):
    string = input()
    group = set()
    for_break = False
    for s in string:
        if s not in group:
            group.add(s)
            pre_string = s
        else:
            if pre_string != s:
                for_break = True
                break
    if not for_break:
        group_word += 1

print(group_word)