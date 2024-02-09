from string import ascii_lowercase
from string import ascii_uppercase

lower = list(ascii_lowercase)
upper = list(ascii_uppercase)
answer = ''

while True:
    word = input()
    if word != '#':
        number = int(upper.index(word[-1]))
        answer = ''
        for i in word[:-1:]:
            if i.isupper():
                answer += upper[(upper.index(i) - number) % 26]
            elif i.islower():
                answer += lower[(lower.index(i) - number) % 26]
            else:
                answer += i
        
        print(answer)

    else:
        break