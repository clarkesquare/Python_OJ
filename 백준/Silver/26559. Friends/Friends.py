for _ in range(int(input())):
    pattern = []
    answer = []
    for _ in range(int(input())):
        tmp = list(input().split())
        tmp[1] = int(tmp[1])
        pattern.append(tmp)
    
    pattern.sort(key=lambda x:x[1], reverse=True)
    for i in pattern:
        answer.append(i[0])
    
    print(*answer, sep=", ")