word = input()
cnt = [0, 0]

for i in range(len(word)-2):
    if word[i] == 'J' and word[i:i+3] == 'JOI':
        cnt[0] += 1
    elif word[i] == 'I' and word[i:i+3] == 'IOI':
        cnt[1] += 1

for j in cnt:
    print(j)