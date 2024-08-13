pattern = {}
word = input()
tmp = ""

for j in range(len(word)):
    for i in range(len(word)-j):
        tmp = word[i:i+j+1:]
        if tmp not in pattern:
            pattern[tmp] = ""

print(len(pattern))