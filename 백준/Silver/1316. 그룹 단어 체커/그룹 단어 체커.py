n = int(input())
answer = 0

for _ in range(n):
    word = input()
    temp = []
    for i in word:
        if i not in temp or temp[-1] == i:
            temp.append(i)
        else:
            break
    if len(temp) == len(word):
        answer += 1

print(answer)