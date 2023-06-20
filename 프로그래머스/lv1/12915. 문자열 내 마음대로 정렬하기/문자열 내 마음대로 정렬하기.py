def solution(strings, n):
    answer = []
    
    strings.sort()
    strings.sort(key= lambda strings: strings[n])
    answer = strings
    return answer