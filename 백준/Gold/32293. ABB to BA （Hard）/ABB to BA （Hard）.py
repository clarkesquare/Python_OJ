from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    word = deque(input().strip('\n'))
    tmp = deque()

    while len(word) != 0:
        if word[0] == 'B':
            if len(tmp) >= 2:
                if tmp[-1] == 'B' and tmp[-2] == 'A':
                    tmp.append(word.popleft())
                    while len(tmp) >= 3:
                        if tmp[-1] == 'B':
                            if tmp[-2] == 'B' and tmp[-3] == 'A':
                                tmp.pop()
                                tmp.pop()
                                word.appendleft(tmp.pop())
                                tmp.append('B')
                            
                            else:
                                break
                        
                        else:
                            break
                
                else:
                    tmp.append(word.popleft())
            
            else:
                tmp.append(word.popleft())
        
        else:
            tmp.append(word.popleft())
    
    print(*(tmp + word), sep='')