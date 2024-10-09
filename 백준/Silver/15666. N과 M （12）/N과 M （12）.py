a, b = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
answer = []

for i in numbers:
    if [i] not in answer:
        answer.append([i])

def nnm():
    global numbers
    global answer
    tmp = []
    for j in answer:
        for k in numbers:
            if j + [k] not in tmp and j[-1] <= k:
                tmp.append(j + [k])

    answer = tmp
    return 0

for _ in range(b-1):
    nnm()

for a in answer:
    print(*a)