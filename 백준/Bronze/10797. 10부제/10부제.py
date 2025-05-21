n = int(input())
numbers = list(map(int, input().split()))
answer = 0

for i in range(5):
    if numbers[i] == n:
        answer += 1

print(answer)