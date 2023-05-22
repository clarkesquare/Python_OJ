def solution(polynomial):
    number = 0
    poly = ''
    temp = ''
    answer = ''
    words = list(map(str, polynomial.split(' ')))
    
    for i in range(0, len(words)):
        if words[i][-1] == 'x' and len(words[i]) > 1:
            poly += int(words[i][:-1:]) * 'x'
        elif words[i][-1] == 'x' and len(words[i]) == 1:
            poly += 'x'
        elif words[i].isnumeric():
            number += int(words[i])

    if poly.count('x') != 0:
        if poly.count('x') == 1:
            temp += str('x')
        else:
            temp = str(poly.count('x')) + str('x')

    if number != 0:
        temp += '+' + str(number)

    if 'x' in temp:
        for i in range(len(temp)):
            if temp[i] == '+':
                answer += ' '
            answer += temp[i]
            if temp[i] == '+':
                answer += ' '
    else:
        answer += str(number)
            
    return answer