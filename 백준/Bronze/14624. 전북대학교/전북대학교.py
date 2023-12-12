n = int(input())

if n % 2 == 1:
    print('*'*n)
    print(' '*((n-1)//2) + '*')
    for i in range(1, (n//2)+1):
        print(' ' * ((n//2)-i) + '*' + (' ' * ((i*2)-1)) + '*')

else:
    print('I LOVE CBNU')