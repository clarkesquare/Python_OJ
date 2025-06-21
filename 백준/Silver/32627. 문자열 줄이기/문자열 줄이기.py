n, m = map(int, input().split())
word = input()
chk = {}
for i in sorted(word)[:m]:
    if i not in chk:
        chk[i] = 1
    
    else:
        chk[i] += 1

for i in word:
    if i in chk:
        chk[i] -= 1
        if chk[i] == 0:
            del chk[i]
    
    else:
        print(i, end='')