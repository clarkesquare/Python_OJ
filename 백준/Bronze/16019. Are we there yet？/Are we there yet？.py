numbers = list(map(int, input().split()))
answer = [0]
temp = []

for i in numbers:
    answer.append(answer[-1] + i)

print(*answer)
for i in numbers:
    temp = []

    for j in range(len(answer)):
        answer[j] -= i

    for k in answer:
        temp.append(abs(k))
    
    print(*temp)