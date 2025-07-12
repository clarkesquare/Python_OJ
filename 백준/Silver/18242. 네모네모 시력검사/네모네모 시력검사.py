n, m = map(int, input().split())
pattern = []
chk = [0, 0]
answer = ''

for i in range(n):
    word = input()
    if '#' in word:
        if answer == '':
            if chk == [0, 0]:
                chk = [word.find('#'), word.rfind('#')]
                if '.' in word[chk[0]:chk[1]+1]:
                    answer = 'UP'

            else:
                if word[chk[0]] != '#':
                    answer = 'LEFT'
                
                elif word[chk[1]] != '#':
                    answer = 'RIGHT'

if answer == '':
    answer = 'DOWN'

print(answer)