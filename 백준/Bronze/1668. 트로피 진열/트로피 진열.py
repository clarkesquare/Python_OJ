trophy = []
max, answer = 0, 0

for _ in range(int(input())):
    trophy.append(int(input()))

max, answer = 0, 0
for i in trophy:
    if i > max:
        max = i
        answer += 1

print(answer)

max, answer = 0, 0
for j in trophy[::-1]:
    if j > max:
        max = j
        answer += 1

print(answer)