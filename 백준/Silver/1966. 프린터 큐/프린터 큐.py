from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    dq = deque()
    a = numbers[m]
    cnt = 0

    for i in range(n):
        dq.append(numbers[i])
    
    numbers.sort(reverse=True)

    while True:
        if dq[0] == numbers[cnt] and dq[0] == a and m == 0:
            cnt += 1
            break
    
        else:
            if dq[0] == numbers[cnt]:
                dq.popleft()
                cnt += 1
            
            else:
                dq.append(dq.popleft())
            
            m -= 1
            if m < 0:
                m = len(dq) - 1

    print(cnt)