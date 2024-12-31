n = int(input())
answer = [0, 0]

pattern = []
pattern_garo = []
pattern_sero = []
tmp = ''
for _ in range(n):
    tmp = input()
    pattern.append(tmp)
    pattern_garo += tmp.split('X')

for j in range(n):
    tmp = ''
    for i in range(n):
        tmp += pattern[i][j]
    
    pattern_sero += tmp.split('X')

for i in pattern_garo:
    if '..' in i:
        answer[0] += 1

for i in pattern_sero:
    if '..' in i:
        answer[1] += 1
    
print(*answer)