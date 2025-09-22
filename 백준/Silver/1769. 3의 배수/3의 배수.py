n = input()
answer = 0
tmp = 0
check = 'NO'

if len(n) == 1:
    if int(n) % 3 == 0:
        check = 'YES'

else:
    while len(n) != 1:
        if int(n) % 3 == 0:
            check = 'YES'
        
        tmp = 0
        answer += 1
        for i in range(len(n)):
            tmp += int(n[i])
        
        n = str(tmp)

print(answer)
print(check)