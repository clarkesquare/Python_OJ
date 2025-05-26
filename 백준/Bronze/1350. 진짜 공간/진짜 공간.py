n = int(input())
files = list(map(int, input().split()))
size = int(input())
answer = 0

for i in files:
    if i != 0:
        if i <= size:
            answer += 1
    
        else:
            answer += i // size
            if i % size != 0:
                answer += 1

print(size * answer)