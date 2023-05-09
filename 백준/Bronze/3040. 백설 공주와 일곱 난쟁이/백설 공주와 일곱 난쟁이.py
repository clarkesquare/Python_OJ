fairies = []
answer, i, j = 0, 0, 0

for _ in range(9):
    fairies.append(int(input()))
answer = sum(fairies) - 100

while True:
    j += 1
    if j == len(fairies):
        i += 1
        j = i + 1
    if fairies[i] + fairies[j] == answer:
        fairies.remove(fairies[j])
        fairies.remove(fairies[i])
        break

for j in fairies:
    print(j)