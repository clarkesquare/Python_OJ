def solution(s, n):
    words_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    words_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    answer = ''

    for i in s:
        temp = 0
        if i.isupper():
            temp = words_upper.index(i)
            temp += n
            if temp >= 26:
                temp -= 26
            answer += words_upper[temp]
        elif i.islower():
            temp = words_lower.index(i)
            temp += n
            if temp >= 26:
                temp -= 26
            answer += words_lower[temp]
        else:
            answer += i
    
    
    return answer