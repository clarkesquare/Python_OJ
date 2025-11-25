n = int(input())
a = []
b = []
c = []
d = []

for i in range(1, n+1):
    scores = list(map(int, input().split()))
    a.append([scores[1], scores[0]])
    b.append([scores[2], scores[0]])
    c.append([scores[3], scores[0]])
    d.append([scores[4], scores[0]])

a = sorted(a, key= lambda x:x[1])
a = sorted(a, key= lambda x: x[0], reverse=True)
b = sorted(b, key= lambda x:x[1])
b = sorted(b, key= lambda x: x[0], reverse=True)
c = sorted(c, key= lambda x:x[1])
c = sorted(c, key= lambda x: x[0], reverse=True)
d = sorted(d, key= lambda x:x[1])
d = sorted(d, key= lambda x: x[0], reverse=True)

answer = []
for i in a:
    if i[1] not in answer:
        answer.append(i[1])
        break

for i in b:
    if i[1] not in answer:
        answer.append(i[1])
        break

for i in c:
    if i[1] not in answer:
        answer.append(i[1])
        break

for i in d:
    if i[1] not in answer:
        answer.append(i[1])
        break

print(*answer)