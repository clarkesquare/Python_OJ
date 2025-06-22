from collections import deque

n = int(input())
answer = 0
chk = 0

for _ in range(n):
    word = deque(input())
    if len(word) % 2 == 0:
        chk = 0
        while len(word) != 0:
            for i in range(len(word)):
                if word[0] == word[1]:
                    word.popleft()
                    word.popleft()
                    break

                elif word[0] == word[-1]:
                    word.popleft()
                    word.pop()
                    break
                
                elif i == len(word) - 1:
                    chk = 1

                else:
                    word.append(word.popleft())
            
            if chk == 1:
                break

        if len(word) == 0:
            answer += 1

print(answer)