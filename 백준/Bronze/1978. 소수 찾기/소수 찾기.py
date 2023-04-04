n = int(input())
numbers = list(map(int, input().split()))
total_cnt = 0

for i in numbers:
    err = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                err += 1
        if err == 0:
            total_cnt += 1

print(total_cnt)