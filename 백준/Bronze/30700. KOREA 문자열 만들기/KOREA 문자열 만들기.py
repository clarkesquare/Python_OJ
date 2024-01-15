korea = 'KOREA'
answer = ''

word = input()
for i in word:
    if i == korea[len(answer) % 5]:
        answer += i

print(len(answer))