from string import ascii_uppercase

answer = 0
alphabets = list(ascii_uppercase)

for _ in range(int(input())):
    answer = 0
    word = input()

    for i in word:
        if i != ' ':
            answer += alphabets.index(i) + 1
    
    print('PERFECT LIFE' if answer == 100 else answer)