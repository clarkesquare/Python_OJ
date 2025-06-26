from collections import deque

while True:
    n, m = map(int, input().split())
    if n != 0 and m != 0:
        numbers = deque(range(1, n+1))
        while len(numbers) != 1:
            for _ in range(m - 1):
                numbers.append(numbers.popleft())
            
            numbers.popleft()
        
        print(numbers[0])
    
    else:
        break