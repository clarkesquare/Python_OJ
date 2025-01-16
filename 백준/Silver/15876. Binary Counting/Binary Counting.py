n, m = map(int, input().split())
tmp = ''
answer = ''
cnt = 0

while len(answer) != 5:
    for i in bin(cnt)[2:]:
        tmp += i
        if len(tmp) == m:
            answer += i
            if len(answer) == 5:
                break
        
        if len(tmp) == n:
            tmp = ''
    
    cnt += 1

for i in answer:
    print(i, end=' ')