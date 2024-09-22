from string import ascii_lowercase
from string import ascii_uppercase

alphabets_lower = list(ascii_lowercase)
alphabets_upper = list(ascii_uppercase)

n, m = map(int, input().split())
word = input()
answer = ""

for i in word:
    if i.islower():
        answer += alphabets_lower[(alphabets_lower.index(i)+n)%26]
    elif i.isupper():
        answer += alphabets_upper[(alphabets_upper.index(i)+n)%26]
    else:
        answer += i

print(answer)