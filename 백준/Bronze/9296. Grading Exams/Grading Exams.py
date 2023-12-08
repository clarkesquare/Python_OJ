answers1 = ''
answers2 = ''
n = 0
cnt = 0

for i in range(1, int(input())+1):
    n = int(input())
    answers1 = input()
    answers2 = input()
    cnt = 0
    for j in range(n):
        if answers1[j] != answers2[j]:
            cnt += 1
    
    print('Case', str(i)+':', cnt)