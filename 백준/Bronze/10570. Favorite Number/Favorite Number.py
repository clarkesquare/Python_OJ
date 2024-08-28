import sys

input = sys.stdin.readline
numbers = {}
answer = []

for _ in range(int(input())):
    numbers = {}
    answer = []
    for _ in range(int(input())):
        a = int(input())
        if a not in numbers:
            numbers[a] = 1
        
        else:
            numbers[a] += 1
    
    answer = list(numbers.items())
    answer.sort(key= lambda x:x[0])
    answer.sort(key= lambda x:x[1], reverse = True)

    print(answer[0][0])