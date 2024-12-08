N, k = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort(reverse = True)

print(numbers[k - 1])