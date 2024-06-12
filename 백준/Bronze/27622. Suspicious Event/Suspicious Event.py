n = int(input())
numbers = list(map(int, input().split()))
answer = 0
tmp = []

for i in numbers:
    if i >= 0:
        tmp.append(i)
    else:
        if abs(i) not in tmp:
            answer += 1
        else:
            tmp.remove(abs(i))

print(answer)