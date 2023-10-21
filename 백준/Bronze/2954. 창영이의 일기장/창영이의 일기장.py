words = list(input())

pattern = ['a', 'e', 'i', 'o', 'u']
answer = ''

for i in range(len(words)):
    if words[i] in pattern and words[i+1] == 'p' and words[i+2] in pattern:
        words[i+1], words[i+2] = '?', '?'

for j in words:
    if j != '?':
        answer += j

print(answer)