from collections import deque

word = deque(input())
chk = input()
tmp = deque()

while len(word) != 0:
    tmp.append(word.popleft())
    if len(tmp) >= len(chk):
        err = 0
        while len(tmp) >= len(chk):
            if chk[-1] == tmp[-1]:
                for i in range(-2, (len(chk) * -1) -1, -1):
                    if chk[i] != tmp[i]:
                        err = 1
                        break
                
                else:
                    for _ in range(len(chk)):
                        tmp.pop()
            
            else:
                break

            if err == 1:
                break

if len(tmp) != 0:
    print(*list(tmp), sep='')

else:
    print('FRULA')