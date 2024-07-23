for _ in range(int(input())):
    input()
    pattern = list(input().split())
    for i in range(5):
        if "machula" in pattern[i]:
            if i == 0:
                pattern[i] = str(int(pattern[4]) - int(pattern[2]))
            elif i == 2:
                pattern[i] = str(int(pattern[4]) - int(pattern[0]))
            else:
                pattern[i] = str(int(pattern[0]) + int(pattern[2]))
            
            break
    
    print(*pattern, sep=" ")