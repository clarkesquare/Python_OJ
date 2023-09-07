numbers = []

for _ in range(7):
    number = int(input())
    if number % 2 == 1:
        numbers.append(number)

if len(numbers) == 0:
    print(-1)
else:
    print(sum(numbers))
    print(min(numbers))