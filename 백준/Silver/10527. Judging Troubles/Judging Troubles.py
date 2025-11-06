n = int(input())

before = {}
answer = 0
for _ in range(n):
    word = input()
    before[word] = before.get(word, 0) + 1

for _ in range(n):
    word = input()
    if word in before:
        if before[word] >= 2:
            before[word] -= 1
        
        else:
            before.pop(word)
        
        answer += 1

print(answer)