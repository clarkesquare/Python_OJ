n = int(input())
word = input()
java = ['J', 'A', 'V']

for i in java:
    if i in word:
        word = word.replace(i, '')

print(word if len(word) != 0 else 'nojava')