n = int(input())

numbers = list(map(int, input().split()))
answer = 0
cnt = 0

for i in numbers:
    if i == 1:
        cnt += 1
        answer += cnt
    
    else:
        cnt = 0

print(answer)