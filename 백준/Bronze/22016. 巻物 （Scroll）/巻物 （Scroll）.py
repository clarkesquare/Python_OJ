a, b = map(int, input().split())
word = input()
b -= 1

answer = word[:b]
for i in word[b:a]:
    if i.islower():
        answer += i.upper()
    else:
        answer += i.lower()

print(answer)