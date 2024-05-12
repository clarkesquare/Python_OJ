a, b = map(int, input().split())
before = list(map(int, input().split()))
after = list(map(int, input().split()))
answer = []

for i in before:
    if i in after and i not in answer:
        answer.append(i)

answer.sort()

for j in answer:
    print(j)