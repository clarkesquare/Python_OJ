temp = []
n = 0
answer = 'false'

while True:
    temp = list(input().split())
    temp[0], temp[2] = int(temp[0]), int(temp[2])
    n += 1
    if temp[1] == '>':
        if temp[0] > temp[2]:
            answer = 'true'
        else:
            answer = 'false'
    
    elif temp[1] == '>=':
        if temp[0] >= temp[2]:
            answer = 'true'
        else:
            answer = 'false'
    
    elif temp[1] == '<':
        if temp[0] < temp[2]:
            answer = 'true'
        else:
            answer = 'false'
    
    elif temp[1] == '<=':
        if temp[0] <= temp[2]:
            answer = 'true'
        else:
            answer = 'false'
    
    elif temp[1] == '==':
        if temp[0] == temp[2]:
            answer = 'true'
        else:
            answer = 'false'
    
    elif temp[1] == '!=':
        if temp[0] != temp[2]:
            answer = 'true'
        else:
            answer = 'false'
    
    elif temp[1] == 'E':
        break

    print(f"Case {n}: {answer}")