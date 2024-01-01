a, b = 0, 0
n = int(input())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)

for i in range(n):
    if i % 2 == 0:
        a += numbers[i]
    else:
        b += numbers[i]

print(a, b)