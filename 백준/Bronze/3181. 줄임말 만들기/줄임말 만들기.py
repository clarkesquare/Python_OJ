pattern = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
words = list(input().split())
answer = words[0][0].upper()

for i in words[1::]:
    if i not in pattern:
        answer += i[0].upper()

print(answer)