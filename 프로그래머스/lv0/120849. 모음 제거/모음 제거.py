def solution(my_string):
    words = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    
    for i in my_string:
        if i in words:
            pass
        else:
            answer += i
    return answer