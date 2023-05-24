while True:
    n = input()
    if n == '0':
        break
    else:
        if n == n[-1::-1]:
            print('yes')
        else:
            print('no')