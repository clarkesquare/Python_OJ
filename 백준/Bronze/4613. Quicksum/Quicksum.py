from string import ascii_uppercase

alphabets = [' '] +list(ascii_uppercase)
answer = 0

while True:
    word = input()
    answer = 0

    if word != '#':
        for i in range(1, len(word)+1):
            answer += i * alphabets.index(word[i-1])
            
        print(answer)

    else:
        break