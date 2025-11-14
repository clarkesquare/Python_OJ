import sys

while True:
    word = input()
    if word != '*':
        answer = 'surprising'
        for i in range(1, len(word)):
            check = {}
            for j in range(len(word)-i):
                tmp = word[j] + word[j+i]
                if tmp not in check:
                    check[tmp] = None
                
                else:
                    answer = 'NOT surprising'
                    break
            
            if answer == 'NOT surprising':
                break

        print(f'{word} is {answer}.')
    
    else:
        break