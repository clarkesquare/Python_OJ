r, c, zr, zc = map(int, input().split())
pattern = []
tmp = ""
answer = []

for _ in range(r):
    pattern.append(input())

for i in pattern:
    tmp = ""
    for j in i:
        tmp += j * zc
    
    for _ in range(zr):
        answer.append(tmp)

for k in answer:
    print(k)