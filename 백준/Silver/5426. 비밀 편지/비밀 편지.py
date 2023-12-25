letters = []
word, answer = '', ''

for _ in range(int(input())):
    letters = []
    word = input()
    answer = ''
    if len(word) == 1:
        answer = word
        
    else:
        for i in range(2, 101):
            if i ** 2 == len(word):
                break
        
        for j in range(0, len(word), i):
            letters.append(word[j:j+i])
        
        for k in range(i-1, -1, -1):
            for l in range(i):
                answer += letters[l][k]
    
    print(answer)