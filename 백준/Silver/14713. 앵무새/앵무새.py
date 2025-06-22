from collections import deque

chk = {}

for i in range(int(input())):
    chk[i] = deque(input().split())

sentence = deque(input().split())

while True:
    for i in chk:
        if chk[i][0] == sentence[0]:
            chk[i].popleft()
            if len(chk[i]) == 0:
                del chk[i]

            sentence.popleft()
            break

    else:
        break
    
    if len(sentence) == 0:
        break

if len(sentence) == 0 and len(chk) == 0:
    print('Possible')

else:
    print('Impossible')