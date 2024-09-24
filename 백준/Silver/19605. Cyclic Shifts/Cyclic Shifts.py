word_sentence = input()
word = input()
pattern = []

for i in range(len(word)):
    pattern.append(word[i:] + word[:i])

for j in pattern:
    if j in word_sentence:
        print("yes")
        break

else:
    print("no")