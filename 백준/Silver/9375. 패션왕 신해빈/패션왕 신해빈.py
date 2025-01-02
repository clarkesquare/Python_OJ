for _ in range(int(input())):
    pattern = {}
    answer = 1
    for _ in range(int(input())):
        a, b = input().split()
        if b not in pattern:
            pattern[b] = 2
        
        else:
            pattern[b] += 1
    
    for i in pattern:
        answer *= pattern[i]
    
    print(answer-1)