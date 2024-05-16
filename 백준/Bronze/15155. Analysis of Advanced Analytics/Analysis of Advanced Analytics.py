n, k = map(int, input().split())
numbers = list(map(int, input().split()))
tmp = 0
answer = 1

for i in range(n):
    if tmp + numbers[i] > k:
        tmp = numbers[i]
        answer += 1
    else:
        tmp += numbers[i]

print(answer)