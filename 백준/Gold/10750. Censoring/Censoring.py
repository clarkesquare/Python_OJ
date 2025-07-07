from collections import deque

word = deque(input())
chk = deque(input())
tmp = deque()

while len(word) != 0:
    tmp.append(word.popleft())
    err = 0
    while len(tmp) >= len(chk):
        if tmp[-1] == chk[-1]:
            for i in range(2, len(chk) + 1):
                if tmp[-1 * i] != chk[-1 * i]:
                    err = 1
                    break
            
            else:
                for _ in range(len(chk)):
                    tmp.pop()
        
        else:
            break

        if err == 1:
            break

print(''.join(tmp))