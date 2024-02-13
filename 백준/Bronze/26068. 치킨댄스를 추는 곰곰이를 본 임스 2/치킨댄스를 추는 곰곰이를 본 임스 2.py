n = int(input())
answer = 0

for _ in range(n):
    a, b = input().split('-')
    if int(b) <= 90:
        answer += 1

print(answer)