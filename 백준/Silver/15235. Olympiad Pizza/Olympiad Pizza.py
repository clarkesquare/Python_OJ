from collections import deque

n = int(input())
numbers = list(map(int, input().split()))
chk = deque()
answer = []
cnt = 0

for i in range(n):
    chk.append([0, i])

while len(chk) != 0:
    cnt += 1
    chk[0][0] += 1
    if numbers[chk[0][1]] == chk[0][0]:
        answer.append([cnt, chk[0][1]])
        chk.popleft()
    
    else:
        chk.append(chk.popleft())

answer.sort(key= lambda x:x[1])
for k, v in answer:
    print(k, end=' ')