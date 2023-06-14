n = int(input())

temp = list(map(int, input().split()))
answer = []

for i in temp:
    if i not in answer:
        answer.append(i)

answer.sort()

for j in answer:
    print(j, end=' ')