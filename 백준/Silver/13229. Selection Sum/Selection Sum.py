n = int(input())
numbers = list(map(int, input().split()))

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(sum(numbers[a:b+1]))