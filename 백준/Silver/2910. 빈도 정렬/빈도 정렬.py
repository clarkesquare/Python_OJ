import sys

input = sys.stdin.readline

a, b = map(int, input().split())
numbers = map(int, input().split())
answer = {}

for i in numbers:
    if i not in answer:
        answer[i] = 1

    else:
        answer[i] += 1
    
tmp = list(answer.items())
tmp.sort(key= lambda x:x[1], reverse=True)

for i in tmp:
    print((str(i[0]) + " ") * i[1], end="")