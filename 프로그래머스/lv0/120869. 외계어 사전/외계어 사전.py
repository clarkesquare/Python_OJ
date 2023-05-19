def solution(spell, dic):
        
    for i in dic:
        answer = 1
        for j in spell:
            if not(j in i and i.count(j) == 1 and answer == 1):
                answer = 2
        if answer == 1:
            break
    return answer