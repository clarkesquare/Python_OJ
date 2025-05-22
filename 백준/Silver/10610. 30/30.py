n = list(map(int, input()))

n.sort(reverse=True)
if n[-1] == 0:
    if sum(n[:-1]) % 3 == 0:
        print(*n, sep='')
    
    else:
        print(-1)

else:
    print(-1)