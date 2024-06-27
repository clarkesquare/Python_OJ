n = int(input())
numbers = []
answer = []
tmp = 0

for _ in range(n):
    numbers.append(int(input()))

for i in range(n):
    tmp = 0
    for j in numbers[:i:]:
        if j < numbers[i]:
            tmp += 1
    
    answer.append(tmp)

print(*answer, sep="\n")