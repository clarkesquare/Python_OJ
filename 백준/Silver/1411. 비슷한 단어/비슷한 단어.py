pattern = []
tmp = []
chk = {}
answer = 0
n = int(input())

for _ in range(n):
    word = input()
    cnt = 0
    tmp = []
    chk = {}
    for i in word:
        if i not in chk:
            cnt += 1
            chk[i] = cnt
        
        tmp.append(chk[i])
    
    pattern.append(tmp)

for i in range(n-1):
    for j in range(i+1, n):
        if pattern[i] == pattern[j]:
            answer += 1

print(answer)