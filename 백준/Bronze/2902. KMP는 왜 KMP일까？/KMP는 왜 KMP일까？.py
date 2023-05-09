word = list(map(str, input().split('-')))
answer = ''

for i in word:
    answer += i[0]

print(answer)