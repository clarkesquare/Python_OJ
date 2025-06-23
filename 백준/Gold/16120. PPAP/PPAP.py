from collections import deque

word = deque(input())
tmp = deque()
answer = 'PPAP'

while True:
    for i in range(len(word)):
        if word[0] == 'A' and len(tmp) >= 2 and len(word) >= 2:
            if tmp[-2] == 'P' and tmp[-1] == 'P' and word[0] == 'A' and word[1] == 'P':
                tmp.pop()
                word.popleft()
                word.popleft()
                break
            
            else:
                tmp.append(word.popleft())
        
        elif word[0] == 'P' and len(tmp) >= 3:
            if tmp[-3] == 'P' and tmp[-2] == 'P' and tmp[-1] == 'A' and word[0] == 'P':
                tmp.pop()
                tmp.pop()
                word.popleft()
                break
            
            else:
                tmp.append(word.popleft())
        
        else:
            tmp.append(word.popleft())

    if len(word) == 0:
        if len(tmp) != 1 or tmp[0] != 'P':
            answer = 'NP'
            
        break

print(answer)