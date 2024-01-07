temp = ''

while True:
    word = list(input().lower().split(' '))
    temp = word[0][0]
    if temp != '*':
        for i in word:
            if i[0] != temp:
                print('N')
                break
        
        else:
            print('Y')
            
    else:
        break