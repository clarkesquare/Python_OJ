from collections import deque

n = int(input())
word = deque(input())
tmp = deque()
answer = 0

while len(word) != 0:
    tmp.append(word.popleft())
    while len(tmp) >= 5:
        if (tmp[-1] == '?' or tmp[-1] == 'p') and (tmp[-2] == '?' or tmp[-2] == 'e') and (tmp[-3] == '?' or tmp[-3] == 'e') and (tmp[-4] == '?' or tmp[-4] == 'k') and (tmp[-5] == 's'):
            for _ in range(5):
                tmp.pop()
            
            tmp.append('?')
            answer += 1
        
        else:
            break

print(answer)