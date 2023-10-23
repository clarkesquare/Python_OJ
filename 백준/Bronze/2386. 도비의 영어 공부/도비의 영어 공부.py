case = []
alphabet = ''
word = ''
answer = 0

while True:
    case = list(input().split())
    if case[0] != '#':    
        alphabet = case[0]
        word = ''
        for i in case[1::]:
            word += i
        
        answer = word.count(alphabet.lower()) + word.count(alphabet.upper())
        print(alphabet, answer)

    else:
        break