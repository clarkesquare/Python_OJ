import sys

input = sys.stdin.readline

n, m = map(int, input().split())
pattern = {}
answer = []

for _ in range(n):
    a, b, c, d = input().strip("\n").split()
    c = int(c)
    d = int(d)
    if a not in pattern:
        pattern[a] = b, c, d
    
    else:
        if pattern[a][1] < c:
            pattern[a] = b, c, d
        
        elif pattern[a][1] == c and pattern[a][2] > d:
            pattern[a] = b, c, d
    

for k, v in pattern.items():
    answer.append([*v])

answer.sort(key = lambda x:x[2])
answer.sort(key = lambda x:x[1], reverse=True)

for i in range(m):
    print(answer[i][0])