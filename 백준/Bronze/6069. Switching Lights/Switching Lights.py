n, m = map(int, input().split())
bulbs = [0] * n
cnt = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    cnt = 0
    if a == 0:
        for i in range(b-1, c):
            if bulbs[i] == 0:
                bulbs[i] = 1
            else:
                bulbs[i] = 0
    
    else:
        for j in range(b-1, c):
            if bulbs[j] == 1:
                cnt += 1
        
        print(cnt)
