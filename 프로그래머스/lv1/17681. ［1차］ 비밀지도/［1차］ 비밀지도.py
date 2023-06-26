def solution(n, arr1, arr2):
    answer = []
    temp = ''
    
    for i in range(len(arr1)):
        arr1[i] = str(bin(arr1[i])[2::])
        arr2[i] = str(bin(arr2[i])[2::])
        if len(arr1[i]) != n:
            arr1[i] = str('0' * (n - len(arr1[i]))) + arr1[i]
        if len(arr2[i]) != n:
            arr2[i] = str('0' * (n - len(arr2[i]))) + arr2[i]
    
    for i in range(n):
        temp = ''
        for j in range(len(arr1[0])):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
        
    return answer