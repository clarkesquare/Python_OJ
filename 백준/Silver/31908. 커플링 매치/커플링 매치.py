fingers = {}
answer = []

for _ in range(int(input())):
    a, b = input().split()
    if b != "-":
        if b not in fingers:
            fingers[b] = [a]
        else:
            fingers[b].append(a)

for i in fingers:
    if len(fingers[i]) == 2:
        answer.append(fingers[i])

print(len(answer))
if len(answer) != 0:
    for j in answer:
        print(*j)