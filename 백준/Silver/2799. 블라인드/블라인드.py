answer = [0, 0, 0, 0, 0]

a, b = map(int, input().split())
pattern = []
cnt = 0

for _ in range(a):
    input()
    pattern = []
    for _ in range(4):
        pattern.append(input()[1:])
    
    for i in range(0, b*5, 5):
        cnt = 0
        for j in range(4):
            if pattern[j][i] == "*":
                cnt += 1
            
            else:
                answer[cnt] += 1
                break
        
        if cnt == 4:
            answer[cnt] += 1
    
input()
print(*answer)