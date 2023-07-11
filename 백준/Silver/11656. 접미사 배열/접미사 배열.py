S = input()
words = []

for i in range(len(S)):
    words.append(S[i::])

words.sort()
for j in words:
    print(j)