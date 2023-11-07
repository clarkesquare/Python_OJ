from string import ascii_uppercase

alphabets = list(ascii_uppercase)
word = input().upper()

for i in alphabets:
    print(i, '|', '*'*word.count(i))