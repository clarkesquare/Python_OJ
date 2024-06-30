for i in range(1, int(input()) + 1):
    n = int(input())
    numbers = list(map(int, input().split()))
    answer = 0
    for j in numbers:
        if numbers.count(j) % 2 == 1:
            answer = j
            break
    
    print(f"Case #{i}: {answer}")