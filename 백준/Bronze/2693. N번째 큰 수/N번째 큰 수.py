n = int(input())
numbers = []

for i in range(n):
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(numbers[8-1])