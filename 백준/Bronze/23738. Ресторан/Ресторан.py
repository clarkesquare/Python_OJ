russian_alphabets = [['B', 'E', 'H', 'P', 'C', 'Y', 'X'], ['v', 'ye', 'n', 'r', 's', 'u', 'h']]
answer = ''

word = input()
for i in word:
    answer += russian_alphabets[1][russian_alphabets[0].index(i)] if i in russian_alphabets[0] else i.lower()

print(answer)