w, n = input().split()
original = []
after = []
tmp = []
check = {2: 5, 5: 2, 1: 1, 8: 8}
n = int(n)

for i in range(n):
    original.append(list(map(int, input().split())))

if w == 'U' or w == 'D':
    for i in range(n-1, -1, -1):
        tmp = []
        for j in range(n):
            if original[i][j] not in check:
                tmp.append('?')
            
            else:
                tmp.append(check[original[i][j]])

        after.append(tmp)

else:
    for i in range(n):
        tmp = []
        for j in range(n-1, -1, -1):
            if original[i][j] not in check:
                tmp.append('?')
            
            else:
                tmp.append(check[original[i][j]])
        
        after.append(tmp)
    

for i in after:
    print(*i)