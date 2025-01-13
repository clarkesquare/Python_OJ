n, m = map(int, input().split())
pattern = list(map(int, input().split())) # 3 0 1 4
answer = []
chk = 0

for i in pattern:
    answer.append(n - i)
# 1 4 3 0

# 왼쪽, 오른쪽으로 번갈아가며 검사해나감
for num in range(n, -1, -1):
    chk = 0
    for i in range(m):
        if num > pattern[i]:
            answer[i] -= 1
            
        else:    
            chk = 1
            break

    if chk == 1:
        for j in range(m-1, -1, -1):
            if num > pattern[j]:
                answer[j] -= 1
            
            else:
                break

print(sum(answer))