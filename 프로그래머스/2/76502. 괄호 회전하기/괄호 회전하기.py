def solution(original):
    answer = 0
    
    for i in range(len(original)):
        s = original[i:] + original[:i]
        check = 0
        while len(s) != 0:
            check = False
            if '()' in s:
                s = s.replace('()', '')
                check = True

            if '[]' in s:
                s = s.replace('[]', '')
                check = True

            if '{}' in s:
                s = s.replace('{}', '')
                check = True

            if not check:
                break

        if len(s) == 0:
            answer += 1
            
    return answer