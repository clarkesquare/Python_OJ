a, b = input().split()
a = int(a)
cnt = 1

while a != int(b):
    cnt += 1
    if b[-1] == "1":
        b = b[:-1]
    
    else:
        if int(b) % 2 == 0:
            b = str(int(b)//2)
        
        else:
            cnt = -1
            break
    
    if a > int(b):
        cnt = -1
        break

print(cnt)