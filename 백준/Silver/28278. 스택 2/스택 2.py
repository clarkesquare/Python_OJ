import sys

input = sys.stdin.readline
numbers = []

for _ in range(int(input())):
    n = input().strip("\n").split()
    if len(n) >= 2:
        n[1] = int(n[1])
        numbers.append(n[1])
    
    else:
        n[0] = int(n[0])
        if n[0] == 2:
            if len(numbers) >= 1:
                print(numbers.pop())
            
            else:
                print(-1)
        
        elif n[0] == 3:
            print(len(numbers))
        
        elif n[0] == 4:
            if len(numbers) == 0:
                print(1)
            
            else:
                print(0)
        
        elif n[0] == 5:
            if len(numbers) >= 1:
                print(numbers[-1])
            
            else:
                print(-1)