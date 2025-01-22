n = int(input())
numbers = list(map(int, input().split()))

for i in range(n):
    tmp = 0

    for j in range(1, numbers[i]):
        if numbers[i] % j == 0:
            tmp += j

    if tmp == numbers[i]:
        print("Perfect")
    
    elif tmp < numbers[i]:
        print("Deficient")
    
    else:
        print("Abundant")