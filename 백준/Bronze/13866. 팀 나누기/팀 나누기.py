numbers = list(map(int, input().split()))

numbers.sort()

print(abs(numbers[0] + numbers[3] - numbers[1] - numbers[2]))