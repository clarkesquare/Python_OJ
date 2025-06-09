from collections import deque

n = int(input())
deq = deque()
num = 0
answer = ''

for _ in range(n):
    number = int(input())
    if number > num:
        while number != num:   
            num += 1 
            deq.appendleft(num)
            answer += '+'
        
        deq.popleft()
        answer += '-'
    
    else:
        if deq[0] == number:
            deq.popleft()
            answer += '-'

        else:
            answer = 'NO'
            break

if answer == 'NO':
    print(answer)

else:
    print(*answer, sep='\n')