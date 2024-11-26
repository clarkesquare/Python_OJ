bingo = []
tmp = []
pattern = []
answer = 0

# 셋팅
for _ in range(5):
    bingo.append(list(map(int, input().split())))

for i in range(5):
    tmp = []
    for j in range(5):
        tmp.append(bingo[j][i])

    bingo.append(tmp)

tmp = [] # 11
for i in range(5):
    tmp.append(bingo[i][i])
    
bingo.append(tmp)

tmp = [] # 12
for i in range(5):
    tmp.append(bingo[i][4-i])
    
bingo.append(tmp)

# 패턴 입력
for _ in range(5):
    pattern += list(map(int, input().split()))

# 게임 시작
for i in range(25):
    for j in range(12):
        if pattern[i] in bingo[j]:
            bingo[j].remove(pattern[i])
            if len(bingo[j]) == 0:
                answer += 1
                if answer == 3:
                    break
    
    if answer == 3:
        break

# 결과 출력
print(i + 1)