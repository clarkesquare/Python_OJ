from string import ascii_uppercase

alphabets = list(ascii_uppercase)
word = []
answer = 0

for _ in range(int(input())):
    word = list(input().split('-'))
    word[1] = int(word[1])
    answer = 0

    for i in range(len(word[0])):
        answer += alphabets.index(word[0][i]) * (26 ** (len(word[0])-i-1))
    
    print('nice' if abs(answer - word[1]) <= 100 else 'not nice')