import sys

input = sys.stdin.readline
pattern = {}
numbers = []

for _ in range(int(input())):
    pattern = {}
    numbers = []
    for _ in range(int(input())):
        a, b = input().split()
        b = int(b)
        if a not in pattern:
            pattern[a] = b
        
        else:
            if pattern[a] > b:
                pattern[a] = b
    
    for k, v in pattern.items():
        numbers.append(v)
    
    numbers.sort()
    print(*numbers)