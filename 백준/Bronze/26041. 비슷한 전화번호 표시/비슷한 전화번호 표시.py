numbers = list(input().split())
n = input()
answer = 0

for i in numbers:
    if n != i and i[:len(n)] == n:
        answer += 1

print(answer)