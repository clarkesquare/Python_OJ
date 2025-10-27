for _ in range(int(input())):
    original = []
    check = []
    answer = 0
    tmp = 1
    n, m = map(int, input().split())
    for _ in range(n):
        original.append(input())
    
    a, b = map(int, input().split())
    for _ in range(a):
        check.append(input())
    
    for i in range(a-n+1):
        for j in range(b-m+1):
            if check[i][j] == original[0][0]:
                tmp = 1
                for k in range(n):
                    for l in range(m):
                        if check[i+k][j+l] != original[k][l]:
                            tmp = 0
                            break
                    
                    if tmp == 0:
                        break
                
                if tmp == 1:
                    answer += 1

    print(answer)