from string import ascii_lowercase

alphabets = list(ascii_lowercase)
answer = 1

word = input()
for i in range(1, len(word)):
    if alphabets.index(word[i]) <= alphabets.index(word[i-1]):
        answer += 1

print(answer)