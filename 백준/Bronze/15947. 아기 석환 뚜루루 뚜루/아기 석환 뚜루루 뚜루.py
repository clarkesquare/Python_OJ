sukhwan = ['baby', 'sukhwan', 'tururu', 'turu', 'very', 'cute', 'tururu', 'turu', 'in', 'bed', 'tururu', 'turu', 'baby', 'sukhwan']

n = (int(input())-1)
a, b = divmod(n, 14)
answer = ''

if sukhwan[b][-2:] == 'ru':
    answer = sukhwan[b] + 'ru' * a
    if answer.count('ru') >= 5:
        answer = 'tu+ru*' + str(answer.count('ru'))
else:
    answer = sukhwan[b]

print(answer)