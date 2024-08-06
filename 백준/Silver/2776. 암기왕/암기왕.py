for _ in range(int(input())):
    a = int(input())
    numbers = set(map(int, input().split()))
    b = int(input())
    test = list(map(int, input().split()))
    for i in test:
        print(1 if i in numbers else 0)