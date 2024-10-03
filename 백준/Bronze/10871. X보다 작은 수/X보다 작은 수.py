a, b = map(int, input().split())

numbers = list(map(int, input().split()))
for i in range(a):
    if numbers[i] < b:
        print(numbers[i], end=" ")