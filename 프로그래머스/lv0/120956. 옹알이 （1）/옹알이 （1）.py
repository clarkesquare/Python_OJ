def solution(babbling):
    voice = ["aya", "ye", "woo", "ma"]
    answer = 0
    temp = ''
    
    for i in babbling:
        temp = i
        check = 0
        for j in voice:
            if j in temp:
                temp = temp.replace(j, '1')
        for k in range(len(temp)):
            if temp[k] != '1' or check != 0:
                check = 2
        if check == 0:
            answer += 1
            
    return answer