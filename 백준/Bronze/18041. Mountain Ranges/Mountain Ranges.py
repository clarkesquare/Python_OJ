n, x = map(int, input().split())
mnts = list(map(int, input().split()))
answer = 1
temp = 1

for i in range(1, n):
    if mnts[i] - mnts[i-1] <= x:
        temp += 1
    else:
        temp = 1
    
    if answer < temp:
        answer = temp

print(answer)