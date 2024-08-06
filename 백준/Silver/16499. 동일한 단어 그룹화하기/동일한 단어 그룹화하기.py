group = {}

for _ in range(int(input())):
    word = input()
    word = "".join(sorted(word))
    if word not in group:
        group[word] = ""

print(len(group))