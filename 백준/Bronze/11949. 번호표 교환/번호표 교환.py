n, m = map(int, input().split())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

for i in range(1, m+1):
    for j in range(1, n):
        if numbers[j-1] % i > numbers[j] % i:
            numbers[j-1], numbers[j] = numbers[j], numbers[j-1]

for k in numbers:
    print(k)