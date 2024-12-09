n, m = map(int, input().split())

original = sorted(list(map(int, input().split())))
answer = []
tmp = []
tmp_answer = []
for i in original:
    if [i] not in answer:
        answer.append([i])

for _ in range(m-1):
    tmp_answer = []
    for i in range(len(answer)):
        for j in original:
            tmp = []
            if answer[i][-1] <= j:
                tmp += answer[i] + [j]

            if tmp not in tmp_answer and len(tmp) != 0:
                tmp_answer.append(tmp)

    answer = tmp_answer

if m == 1:
    for i in answer:
        print(*i)

else:
    for i in answer:
        for j in range(len(original)):
            if i.count(original[j]) > original.count(original[j]):
                break

        else:
            print(*i)