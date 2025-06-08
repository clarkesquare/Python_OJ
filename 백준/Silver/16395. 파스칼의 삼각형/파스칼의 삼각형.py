n, k = map(int, input().split())

check = [[1]]
tmp = [1]
for i in range(1, n+1):
    tmp = [1]
    for j in range(1, i):
        if j != i - 1:
            tmp.append(check[i-1][j] + check[i-1][j-1])
            
        else:
            tmp.append(1)
    
    check.append(tmp)

print(check[n][k-1])