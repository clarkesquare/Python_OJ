numbers = []
cnt = 0
answer = 0.000

for _ in range(int(input())):
    numbers = list(map(int, input().split()))
    cnt = 0
    for i in numbers[1::]:
        if i > sum(numbers[1:])/numbers[0]:
            cnt += 1

    answer = (cnt * 100) / numbers[0]
    print(f"{answer:.3f}%")