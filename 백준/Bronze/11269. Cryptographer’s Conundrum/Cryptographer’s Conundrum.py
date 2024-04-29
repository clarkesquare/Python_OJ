answer = 0

word = input()
for i in range(len(word)):
    if i % 3 == 0 and word[i] != "P":
        answer += 1
    elif i % 3 == 1 and word[i] != "E":
        answer += 1
    elif i % 3 == 2 and word[i] != "R":
        answer += 1

print(answer)