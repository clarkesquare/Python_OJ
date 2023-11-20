letter = input()
pattern = ['B', 'C', 'D', 'F']

if 'A' in letter:
    for i in pattern:
        letter = letter.replace(i, 'A')

elif 'B' in letter:
    for j in pattern[1::]:
        letter = letter.replace(j, 'B')

elif 'C' in letter:
    for k in pattern[2::]:
        letter = letter.replace(k, 'C')

else:
    letter = 'A' * len(letter)

print(letter)