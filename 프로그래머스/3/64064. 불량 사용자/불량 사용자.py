from itertools import permutations

def solution(user_id, banned_id):
    list_banned_id = list(permutations(user_id, len(banned_id)))
    
    set_banned_id = set()
    for case in list_banned_id:
        for_break = False
        for i in range(len(banned_id)):
            for j in range(len(case[i])):
                if len(case[i]) == len(banned_id[i]) and (case[i][j] == banned_id[i][j] or banned_id[i][j] == '*'):
                    continue
                else:
                    for_break = True
                    break
            if for_break:
                break
            if i == len(banned_id) - 1:
                set_banned_id.add(tuple(sorted(case)))
    
    return len(set_banned_id)