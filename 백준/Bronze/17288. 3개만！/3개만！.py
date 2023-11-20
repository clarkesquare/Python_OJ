numbers = list(map(int, input()))
cnt = 0

for i in range(3, len(numbers)):
    if (numbers[i-3] == numbers[i-2] - 1) and (numbers[i-2] == numbers[i-1] - 1) and (numbers[i - 1] == numbers[i] - 1):
        numbers[i-3], numbers[i-2], numbers[i-1], numbers[i] = 99, 99, 99, 99
    elif (numbers[i-3] == numbers[i-2] - 1) and (numbers[i-2] == numbers[i-1] - 1) and (numbers[i - 1] != numbers[i] - 1):
        cnt += 1

if (numbers[-3] == numbers[-2] - 1) and (numbers[-2] == numbers[-1] - 1):
    cnt += 1

print(cnt)