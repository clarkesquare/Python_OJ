n = int(input())
tmp = {}
answer = []

for i in range(n+1):
    for j in range(1, n+1):
        if i/j not in tmp and i <= j:
            tmp[i/j] = str(i) + "/" + str(j)

for k, v in tmp.items():
    answer.append([v, k])

answer.sort(key= lambda x:x[1])

print(len(answer))
for a in answer:
    print(a[0])