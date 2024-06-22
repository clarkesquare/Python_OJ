name = []
cnt = []
answer = []

for _ in range(int(input())):
    tmp = input()
    if tmp not in name:
        name.append(tmp)
        cnt.append(1)
    else:
        cnt[name.index(tmp)] += 1

for i in range(len(name)):
    if cnt[i] == max(cnt):
        answer.append(name[i])

answer.sort()
print(*answer, sep="\n")