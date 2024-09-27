n = int(input())

numbers = list(map(int, input().split()))
min = 99999999999999
numbers.sort()
for _ in range(n):
    if numbers[0] + numbers[-1] < min:
        min = numbers[0] + numbers[-1]

    numbers.pop(0)
    numbers.pop(-1)

print(min)