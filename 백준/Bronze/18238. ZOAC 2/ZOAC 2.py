from string import ascii_uppercase

alphabets = list(ascii_uppercase)

word = input()
answer = 0
temp = 'A'

for i in word:
    minus = abs(alphabets.index(i) - alphabets.index(temp))
    if minus >= 14:
        answer += 26 - minus
    else:
        answer += minus
    
    temp = i

print(answer)