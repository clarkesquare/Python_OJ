a = input()
b = input()
anagram = [[], []]

for i in a:
    if i != " ":
        anagram[0].append(i)

for j in b:
    if j != " ":
        anagram[1].append(j)

anagram[0].sort()
anagram[1].sort()

print("Is an anagram." if anagram[0] == anagram[1] else "Is not an anagram.")