max_length = 0
words = []

for i in range(5):
    words.append(list(input()))
    if len(words[i]) > max_length:
        max_length = int(len(words[i]))

for i in range(5):
    if len(words[i]) < max_length:
        for j in range(max_length - len(words[i])):
            words[i].append('?')

for i in range(max_length):
    for j in range(5):
        if words[j][i] != '?':
            print(words[j][i], end='')