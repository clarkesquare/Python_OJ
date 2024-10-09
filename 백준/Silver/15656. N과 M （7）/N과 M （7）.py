a, b = map(int, input().split())
pattern = sorted(list(map(int, input().split())))
answer = [[i] for i in pattern]
tmp = []

def nnm():
    global pattern
    global answer
    tmp = []
    for i in answer:
        for j in pattern:
            tmp.append(i+ [j])

    answer = tmp
    return 0

for _ in range(b-1):
    nnm()

for a in answer:
    print(*a)