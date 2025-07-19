from itertools import combinations
answer = []

for i in range(1, int(input()) + 1):
    numbers = list(map(int, input().split()))
    chk = combinations(numbers, 3)
    tmp = 0
    for j in chk:
        if int(str(sum(j))[-1]) > tmp:
            tmp = int(str(sum(j))[-1])
    
    answer.append(tmp)

chk = max(answer)
for i in range(len(answer) - 1, -1, -1):
    if answer[i] == chk:
        print(i + 1)
        break