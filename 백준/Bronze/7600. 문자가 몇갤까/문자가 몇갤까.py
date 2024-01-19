word = ''
temp = []
answer = 0

while True:
    word = input().lower()
    temp = []
    if word != '#':
        answer = 0
        for i in word:
            if i.isalpha() and i not in temp:
                answer += 1
                temp.append(i)
        
        print(answer)
    else:
        break