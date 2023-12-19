word = input()
temp = word[0]
answer = ''

for i in range(1, len(word)):
    if temp != word[i]:
        answer += temp
        temp = word[i]

answer += temp
print(answer)