n, m = map(int, input().split())
pattern = []
for _ in range(n):
    pattern.append(list(input()))

for i in range(m):
    for j in range(n-1, 0, -1):
        if pattern[j][i] == '.':
            for k in range(j-1, -1, -1):
                if pattern[k][i] == 'o':
                    pattern[j][i] = 'o'
                    pattern[k][i] = '.'
                    break
                
                elif pattern[k][i] == '#':
                    break

for l in pattern:
    print(*l, sep='')