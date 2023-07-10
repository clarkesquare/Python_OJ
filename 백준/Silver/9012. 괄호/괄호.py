for _ in range(int(input())):
    word = input()
    while '()' in word:
        word = word.replace('()', '')
    if len(word) == 0:
        print('YES')
    else:
        print('NO')