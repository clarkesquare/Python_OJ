a, b = map(int, input().split())
numbers = list(map(int, input().split()))

for i in numbers:
    if i < b:
        print(str(i), end=' ')