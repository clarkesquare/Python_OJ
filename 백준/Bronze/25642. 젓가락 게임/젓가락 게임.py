a, b = map(int, input().split())
cnt = 0

while a < 5 and b < 5:
    cnt += 1
    if cnt % 2 == 0:
        a += b
    
    else:
        b += a

if a >= 5:
    print('yj')

else:
    print('yt')