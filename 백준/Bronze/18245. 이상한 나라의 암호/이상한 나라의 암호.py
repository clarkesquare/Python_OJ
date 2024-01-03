answer = ''
cnt = 1

while True:
    word = input()
    if word != 'Was it a cat I saw?':
        cnt += 1
        answer = ''.join(word[::cnt])
        print(answer)
        
    else:
        break