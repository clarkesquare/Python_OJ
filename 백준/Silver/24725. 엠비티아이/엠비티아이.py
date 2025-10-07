MBTI = [{'E': None, 'I': None}, {'N': None, 'S': None}, {'F': None, 'T': None}, {'P': None, 'J': None}]
answer = 0

n, m = map(int, input().split())
pattern = []
for _ in range(3):
    pattern.append('X' * (m + 6))

for _ in range(n):
    pattern.append('X' * 3 + input() + 'X' * 3)

for _ in range(3):
    pattern.append('X' * (m + 6))

for i in range(3, n+4):
    for j in range(3, m+4):
        if pattern[i][j] in MBTI[0]:
            if (pattern[i][j-1] in MBTI[1]) and (pattern[i][j-2] in MBTI[2]) and (pattern[i][j-3] in MBTI[3]):
                answer += 1
            
            if (pattern[i-1][j-1] in MBTI[1]) and (pattern[i-2][j-2] in MBTI[2]) and (pattern[i-3][j-3] in MBTI[3]):
                answer += 1
            
            if (pattern[i-1][j] in MBTI[1]) and (pattern[i-2][j] in MBTI[2]) and (pattern[i-3][j] in MBTI[3]):
                answer += 1
            
            if (pattern[i-1][j+1] in MBTI[1]) and (pattern[i-2][j+2] in MBTI[2]) and (pattern[i-3][j+3] in MBTI[3]):
                answer += 1
            
            if (pattern[i][j+1] in MBTI[1]) and (pattern[i][j+2] in MBTI[2]) and (pattern[i][j+3] in MBTI[3]):
                answer += 1
            
            if (pattern[i+1][j+1] in MBTI[1]) and (pattern[i+2][j+2] in MBTI[2]) and (pattern[i+3][j+3] in MBTI[3]):
                answer += 1
            
            if (pattern[i+1][j] in MBTI[1]) and (pattern[i+2][j] in MBTI[2]) and (pattern[i+3][j] in MBTI[3]):
                answer += 1
            
            if (pattern[i+1][j-1] in MBTI[1]) and (pattern[i+2][j-2] in MBTI[2]) and (pattern[i+3][j-3] in MBTI[3]):
                answer += 1

print(answer)