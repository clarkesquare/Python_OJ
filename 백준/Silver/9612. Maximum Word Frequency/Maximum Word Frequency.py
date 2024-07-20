words = []
tmp = []
word = ""

for _ in range(int(input())):
    word = input()
    if word not in tmp:
        words.append([word, 1])
        tmp.append(word)

    else:
        words[tmp.index(word)][1] += 1

words.sort(key = lambda x:x[0])
words.sort(key = lambda x:x[1])

print(*words[-1])