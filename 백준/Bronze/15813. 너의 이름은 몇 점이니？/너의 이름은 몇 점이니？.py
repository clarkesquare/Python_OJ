from string import ascii_uppercase

n = int(input())
name = input()
alphabets = list(ascii_uppercase)
answer = 0

for i in name:
    answer += alphabets.index(i) + 1

print(answer)