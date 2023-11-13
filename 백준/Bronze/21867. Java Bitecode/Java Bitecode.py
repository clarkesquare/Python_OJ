n = int(input())
word = input()
java = ['J', 'A', 'V']
temp = word

for i in java:
    if i in temp:
        temp = temp.replace(i, '')

print(temp if len(temp) != 0 else 'nojava')