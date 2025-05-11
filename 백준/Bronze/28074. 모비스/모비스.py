word = ['M', 'O', 'B', 'I', 'S']

for i in input():
    if i in word:
        word.remove(i)

if len(word) == 0:
    print('YES')

else:
    print('NO')