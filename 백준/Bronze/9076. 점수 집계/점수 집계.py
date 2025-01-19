n = int(input()) # 4

for _ in range(n): # 10 8 5 7 9 // 1 2 3 6 9
    numbers = list(map(int, input().split()))
    numbers.sort()
    # numbers에서 3번 인덱스에서 1번 인덱스를 뺀 값이 4 이상인지 검사
    if numbers[3] - numbers[1] >= 4:
        print("KIN")
    
    else:
        print(sum(numbers[1:4]))