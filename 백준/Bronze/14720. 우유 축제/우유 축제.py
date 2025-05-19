n = int(input())
answer = 0

numbers = list(map(int, input().split()))

for i in range(n):
    if answer % 3 == numbers[i]:
        answer += 1

print(answer)