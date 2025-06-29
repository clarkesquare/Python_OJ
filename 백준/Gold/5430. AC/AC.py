from collections import deque
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    pattern = deque(input().strip('\n'))
    n = int(input())
    array = input().strip('\n')[1:-1]
    chk = 0
    if len(array) != 0:
        array = deque(array.split(','))
    
    else:
        array = deque()

    for i in range(len(pattern)):
        if pattern[0] == 'R':
            chk = (chk + 1) % 2
        
        else:
            if len(array) == 0:
                break

            elif chk == 0:
                array.popleft()
            
            else:
                array.pop()
        
        pattern.popleft()
    
    if len(pattern) != 0:
        print('error')
    
    else:
        print('[', end='')
        if chk == 0:
            print(*array, sep=',', end='')
        
        else:
            array = list(array)[::-1]
            print(*array, sep=',', end='')

        print(']')