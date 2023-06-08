numbers = list(map(int, input().split()))

while numbers != sorted(numbers):
    for i in range(len(numbers)-1):
        cnt = 0
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            cnt = 1
        if cnt == 1:
            for j in numbers:
                print(j, end=' ')
            print('')