import copy

n, h, w = map(int, input().split())
chk = ['?'] * n * w
chk = copy.deepcopy(chk)
answer = ''

for _ in range(h):
    word = input()
    for i in range(len(word)):
        if word[i] != '?' and chk[i] == '?':
            chk[i] = word[i]

for i in range(n):
    for j in range(w):
        if chk[i*w+j] != '?':
            answer += chk[i*w+j]
            break

    else:
        answer += '?'

print(answer)