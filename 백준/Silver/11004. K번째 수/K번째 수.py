n, m = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()
print(numbers[m-1])