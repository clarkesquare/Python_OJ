from collections import deque

while True:
    n = int(input())
    if n != 0:
        name = {}
        chk = {}
        numbers = []
        pattern = deque()
        for _ in range(n):
            a, b = input().split()
            b = int(b)
            name[a.lower()] = a
            chk[a.lower()] = b
        
        numbers = list(chk.items())
        numbers.sort(key= lambda x:x[0])
        numbers.sort(key= lambda x:x[1], reverse=True)
        for i in range(len(numbers)):
            if i % 2 == 0:
                pattern.append(name[numbers[i][0]])
            
            else:
                pattern.appendleft(name[numbers[i][0]])
        
        print(*pattern)
    
    else:
        break