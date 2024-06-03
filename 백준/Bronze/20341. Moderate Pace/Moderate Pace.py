n = int(input())

answer = []
tmp = []
numbers = []
for _ in range(n):
    numbers.append([])

for _ in range(3):
    tmp = list(map(int, input().split()))
    for i in range(n):
        numbers[i].append(tmp[i])


for j in numbers:
    j.sort()
    answer.append(j[1])

print(*answer)