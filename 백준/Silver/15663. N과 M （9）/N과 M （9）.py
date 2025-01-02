n, m = map(int, input().split())

original = {}
answer = ()
tmp = ()

for i in sorted(list(map(int, input().split()))):
    if i not in original:
        original[i] = 1
        answer += (i, )
    
    else:
        original[i] += 1

for i in range(m-1):
    tmp = {}
    if i == 0:
        for j in answer:
            for k in original:
                if (j, ) + (k,) not in tmp:
                    tmp[(j, ) + (k,)] = ''
    
    else:
        for j in answer:
            for k in original:
                if j + (k,) not in tmp:
                    tmp[j + (k,)] = ''
    
    answer = tmp

if m != 1:
    for i in answer:
        for j in original:
            if i.count(j) > original[j]:
                break
        
        else:
            print(*i)

else:
    print(*answer, sep='\n')