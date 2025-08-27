n = int(input())
pattern = []
answer = 0

for _ in range(4):
    pattern.append('X' * (n + 8))

for _ in range(n):
    pattern.append('X' * 4 + input() + 'X' * 4)

for _ in range(4):
    pattern.append('X' * (n + 8))

for i in range(4, n+4):
    for j in range(4, n+4):
        if pattern[i][j] == 'M':
            if pattern[i-1][j-1] == 'O' and pattern[i-2][j-2] == 'B' and pattern[i-3][j-3] == 'I' and pattern[i-4][j-4] == 'S':
                answer += 1
        
            if pattern[i][j-1] == 'O' and pattern[i][j-2] == 'B' and pattern[i][j-3] == 'I' and pattern[i][j-4] == 'S':
                answer += 1
            
            if pattern[i+1][j-1] == 'O' and pattern[i+2][j-2] == 'B' and pattern[i+3][j-3] == 'I' and pattern[i+4][j-4] == 'S':
                answer += 1
            
            if pattern[i+1][j] == 'O' and pattern[i+2][j] == 'B' and pattern[i+3][j] == 'I' and pattern[i+4][j] == 'S':
                answer += 1
            
            if pattern[i+1][j+1] == 'O' and pattern[i+2][j+2] == 'B' and pattern[i+3][j+3] == 'I' and pattern[i+4][j+4] == 'S':
                answer += 1
            
            if pattern[i][j+1] == 'O' and pattern[i][j+2] == 'B' and pattern[i][j+3] == 'I' and pattern[i][j+4] == 'S':
                answer += 1
            
            if pattern[i-1][j+1] == 'O' and pattern[i-2][j+2] == 'B' and pattern[i-3][j+3] == 'I' and pattern[i-4][j+4] == 'S':
                answer += 1
            
            if pattern[i-1][j] == 'O' and pattern[i-2][j] == 'B' and pattern[i-3][j] == 'I' and pattern[i-4][j] == 'S':
                answer += 1

print(answer)