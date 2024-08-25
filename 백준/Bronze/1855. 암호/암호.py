n = int(input())

word = input()
tmp = []
answer = ""

for i in range(0, len(word)//n):
    if i % 2 == 0:
        tmp.append(word[i * n:(i + 1) * n])
    else:
        tmp.append(word[i * n:(i + 1) * n][::-1])

for j in range(n):
    for i in range(len(word)//n):
        answer += tmp[i][j]

print(answer)