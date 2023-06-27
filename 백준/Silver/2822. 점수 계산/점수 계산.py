score, temp = [], []

for i in range(8):
    score.append(int(input()))
    temp.append(score[i])

temp.sort(reverse=True)
print(sum(temp[:5:]))

for j in range(len(score)):
    if score[j] in temp[:5:]:
        print(j+1, end=' ')