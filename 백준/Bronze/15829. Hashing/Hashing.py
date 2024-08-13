from string import ascii_lowercase

alphabets = list(ascii_lowercase)

n = int(input())
word = input()
answer = 0

for i in range(n):
    answer += (alphabets.index(word[i])+1) * (31 ** i)

print(answer)