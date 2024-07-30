n, m, k = map(int, input().split())
answer = 0
tmp = ""

for _ in range(n):
    tmp = input()
    for i in range(m-k+1):
        if tmp[i] == "0" and tmp[i:i+k] == "0" * k:
            answer += 1
    
print(answer)