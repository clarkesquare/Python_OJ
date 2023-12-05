from string import ascii_lowercase

word, alphabets = [], []
answer = ''

for i in range(int(input())):
    word = list(input().lower())
    alphabets = list(ascii_lowercase)
    answer = ''

    for i in word:
        if i in alphabets:
            alphabets.remove(i)

    answer = ''.join(alphabets)    
    if len(answer) == 0:
        print('pangram')
    else:
        print('missing', answer)