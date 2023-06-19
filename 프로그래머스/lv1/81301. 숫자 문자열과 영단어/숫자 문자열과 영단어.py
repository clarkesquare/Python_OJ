def solution(s):
    answer = ''
    temp = ''
    
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in s:
        if i.isnumeric():
            answer += i
        else:
            temp += i
            if temp in numbers:
                answer += str(numbers.index(temp))
                temp = ''

    answer = int(answer)
    return answer