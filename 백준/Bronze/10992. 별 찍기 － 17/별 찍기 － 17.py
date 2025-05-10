n = int(input())


# 처음
if n == 1:
    print('*')

else:
    print(' ' * (n - 1) + '*')
    
    # 중앙
    for i in range(n-2):
        print(' ' * (n - 2 - i) + '*' + ' ' * (1 + 2 * i) + '*')

    # 끝
    print('*' * (2 * (n - 1) + 1))