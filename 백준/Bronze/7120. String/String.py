word = input()
answer = ''

for i in range(1, len(word)):
    if word[i] != word[i-1]:
        answer += word[i-1]

answer += word[-1]
print(answer)