numbers = []
cnt = 0

for _ in range(int(input())):
    n = int(input())
    cnt += 1
    numbers = list(map(int, input().split()))
    for i in numbers:
        if numbers.count(i) % 2 == 1:
            print(f"Case #{cnt}: {i}")
            break