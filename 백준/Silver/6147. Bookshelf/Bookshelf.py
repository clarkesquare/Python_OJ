n, b = map(int, input().split())
numbers = []
answer = 0

for _ in range(n):
    numbers.append(int(input()))

numbers.sort(reverse=True)

for i in range(b):
    answer += numbers[i]
    if answer >= b:
        break

print(i+1)