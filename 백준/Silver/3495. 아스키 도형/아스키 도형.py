n, m = map(int, input().split())
answer = 0
tmp = 0

for _ in range(n):
    word = input()
    for i in range(m):
        if word[i] == "/" or word[i] == "\\":
            answer += 0.5
            if tmp == 0:
                tmp = 1
            
            else:
                tmp = 0
        
        else:
            if tmp == 1:
                answer += 1

print(int(answer))