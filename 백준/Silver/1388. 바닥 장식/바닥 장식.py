n, m = map(int, input().split())
pattern = []
answer = 0

for _ in range(n):
    pattern.append(list(input()))

for i in range(n):
    for j in range(m):
        if pattern[i][j] == '-':
            pattern[i][j] = '*'
            for k in range(j+1, m):
                if pattern[i][k] == '-':
                    pattern[i][k] = '*'
                
                else:
                    break
            
            answer += 1
        
        elif pattern[i][j] == '|':
            pattern[i][j] = '*'
            for k in range(i+1, n):
                if pattern[k][j] == '|':
                    pattern[k][j] = '*'
                
                else:
                    break
            
            answer += 1

print(answer)