n, m = map(int, input().split())
numbers = list(map(int, input().split()))
minimum = 99999999

for i in range(n-1):
    if minimum > numbers[i] + numbers[i+1]:
        minimum = numbers[i] + numbers[i+1]

print(minimum * m)