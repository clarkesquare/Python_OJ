n = int(input())

pattern = {}

for _ in range(n):
    a, b = map(int, input().split())
    if a == 1:
        for i in range(b, b+4):
            if i not in pattern:
                pattern[i] = 0
        
        maximum = max(pattern[b], pattern[b+1], pattern[b+2], pattern[b+3])
        for i in range(b, b+4):
            pattern[i] = maximum + 1
    
    elif a == 2:
        if b not in pattern:
            pattern[b] = 4
        
        else:
            pattern[b] += 4
    
    else:
        if b not in pattern:
            print(0)
        
        else:
            print(pattern[b])