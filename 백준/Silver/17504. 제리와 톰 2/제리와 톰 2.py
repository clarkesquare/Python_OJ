n = int(input())
numbers = [1] + list(map(int, input().split()))
numbers = numbers[::-1]

a = numbers[1]
b = 1
c = numbers[0]

for i in range(2, n+1):
    a, b, c = numbers[i], c, a * c + b

print(a * c - b, c)