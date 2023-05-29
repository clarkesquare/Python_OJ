def solution(array, commands):
    answer = []
    
    for n in commands:
        temp = []
        i, j, k = n[0]-1, n[1], n[2]-1
        temp = array[i:j]
        temp.sort()
        answer.append(temp[k])
    return answer