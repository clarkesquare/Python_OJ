n, k = map(int, input().split())
numbers = list(range(2, n+1))
cnt = 0
temp = 0
answer = 0

while cnt != k:
    if temp == 0:
        temp = numbers[0]
    for i in numbers:
        if i % temp == 0:
            cnt += 1
            answer = i
            numbers.remove(i)
            break
    else:
        temp = 0

print(answer)