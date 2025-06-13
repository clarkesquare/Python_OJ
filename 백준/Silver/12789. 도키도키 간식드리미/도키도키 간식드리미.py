from collections import deque

n = int(input())
numbers = deque((map(int, input().split())))
tmp = deque()
answer = 'Nice'
cnt = 1

while True:
    if len(numbers) != 0 and numbers[0] == cnt:
        cnt += 1
        numbers.popleft()
    
    elif len(tmp) != 0 and tmp[0] == cnt:
        cnt += 1
        tmp.popleft()
    
    else:
        if len(numbers) != 0:
            tmp.appendleft(numbers.popleft())

        elif len(tmp) == 0:
            break

        else:
            answer = 'Sad'
            break
        
print(answer)