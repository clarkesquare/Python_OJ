pattern = []
answer = []

pattern += input().split()
pattern += input().split()

for i in pattern:
    for j in pattern:
        if [i, j] not in answer:
            answer.append([i, j])

answer.sort(key=lambda x:x[1])
answer.sort(key=lambda x:x[0])

for i in answer:
    print(*i)