n = int(input())
check = {}
answer = 0
tmp = []

for i in list(map(int, input().split())):
    if i != 0:
        if i not in check:
            check[i] = 1
            if answer == 0:
                answer = i
            
            else:
                if answer > i:
                    answer = i
        
        else:
            check[i] += 1

while True:
    if answer * 2 in check:
        answer *= 2
        check[answer] += check[answer//2] //2
    
    else:
        if check[answer] >= 2:
            answer *= 2
            check[answer] = check[answer//2] //2
        
        else:
            break

for k, v in check.items():
    tmp.append(k)

print(max(tmp))