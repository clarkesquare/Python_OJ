def solution(array, n):
    array.sort()
    temp = []
    
    for i in array:
        temp.append((abs(n-i)))
    
    answer = array[temp.index(min(temp))]
    return answer