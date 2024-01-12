n, m = map(int, input().split())
pattern = []
temp = 0
answer = 0
for _ in range(m):
    pattern.append(input())

for i in pattern:
    temp = 0
    for j in i:
        if j.isupper():
            temp += 4
        elif j.islower() or j.isnumeric():
            temp += 2
        else:
            temp += 1
    
    if temp <= n:
        answer += 1

print(answer)