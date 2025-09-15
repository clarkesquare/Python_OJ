check = {}
answer = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    if b == 1:
        if a not in check:
            check[a] = None
        
        else:
            answer += 1
    
    elif b == 0:
        if a in check:
            check.pop(a)
        
        else:
            answer += 1

print(answer + len(check))