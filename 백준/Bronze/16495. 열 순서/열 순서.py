from string import ascii_uppercase

alphabets = list(ascii_uppercase)
answer = 0

word = input()[::-1]
for i in range(len(word)):
    answer += (alphabets.index(word[i]) + 1) * (26 ** i)

print(answer)