word = input()

word = word.replace('pi', '.')
word = word.replace('ka', '.')
word = word.replace('chu', '.')

if len(word) == word.count('.'):
    print('YES')

else:
    print('NO')