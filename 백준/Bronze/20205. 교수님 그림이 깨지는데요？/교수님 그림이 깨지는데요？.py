import copy

a, b = map(int, input().split())
answer = []

for _ in range(a):
    word = input().split()
    for _ in range(b):
        tmp = ''
        for i in word:
            tmp += i * b
        
        answer.append(copy.deepcopy(tmp))
    
for j in answer:
    print(*j)