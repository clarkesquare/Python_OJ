from string import ascii_uppercase, ascii_lowercase

alphabets = list(" " + ascii_uppercase + ascii_lowercase)
n = int(input())
words = list(map(int, input().split()))
word = input()
pattern = {}
answer = "y"

for i in words:
    if alphabets[i] not in pattern:
        pattern[alphabets[i]] = 1
    
    else:
        pattern[alphabets[i]] += 1

for j in word:
    if j in pattern and pattern[j] >= 1:
        pattern[j] -= 1
    
    else:
        answer = "n"
        break

print(answer)