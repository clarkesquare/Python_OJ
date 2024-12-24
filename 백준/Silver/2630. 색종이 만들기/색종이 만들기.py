n = int(input())
original = n
pattern = []
cnt = [0, 0]

for _ in range(n):
    pattern.append(list(map(int, input().split())))

while n != 0:
    for i in range(0, original, n):
        for j in range(0, original, n):
            if pattern[i][j] != 'a':
                tmp = []
                for a in range(i, i + n):
                    tmp += pattern[a][j:j+n]
                
                if tmp.count(tmp[0]) == n ** 2:
                    if tmp[0] == 0:
                        cnt[0] += 1
                    
                    else:
                        cnt[1] += 1
                
                    for a in range(i, i + n):
                        for b in range(j, j+n):
                            pattern[a][b] = 'a'
    
    n //= 2

print(*cnt, sep="\n")