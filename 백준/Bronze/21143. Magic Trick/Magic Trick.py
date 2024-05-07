word = input()
answer = 1

for i in word:
    if word.count(i) >= 2:
        answer = 0
        break

print(answer)