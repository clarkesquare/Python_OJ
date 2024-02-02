for _ in range(int(input())):
    n, m = input().split()
    n = list(n)
    temp = []
    answer = 'YES'
    for i in m:
        if i in n:
            if i not in temp:
                temp.append(i)
        else:
            answer = 'NO'
            break
    
    n.sort()
    temp.sort()
    if n != temp:
        answer = 'NO'
    
    print(answer)