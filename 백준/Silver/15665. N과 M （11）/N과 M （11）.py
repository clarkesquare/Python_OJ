n, m = map(int, input().split())
original = list(map(int, input().split()))
original.sort()
answer = {}
tmp = {}

for i in original:
    if i not in answer:
        answer[(i,)] = ''

for i in range(m-1):
    tmp = {}
    for k in answer:
        for j in original:
            if k + (j, ) not in tmp:
                tmp[(k)+(j, )] = ''
    
    answer = tmp

for i in answer:
    print(*i)