def solution(babbling):
    pattern = ['aya', 'ye', 'woo', 'ma']
    answer = 0
    temp = ''
    
    for i in range(len(babbling)):
        temp = babbling[i]
        for j in range(len(pattern)):
            if pattern[j] in babbling[i]:
                temp = temp.replace(pattern[j], str(j))
    
        if temp.isnumeric():
            for k in range(1, len(temp)):
                if temp[k-1] == temp[k]:
                    break
            else:
                answer += 1

    return answer