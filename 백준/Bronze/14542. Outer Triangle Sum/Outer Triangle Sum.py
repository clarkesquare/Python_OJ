i = 0

while True:
    n = int(input())
    if n != 0:
        i += 1
        numbers = []
        answer = 0
        for _ in range(n):
            tmp = list(map(int, input().split()))
            tmp += [0] * (n - len(tmp))
            numbers.append(tmp)
        
        for j in range(n):
            answer += numbers[j][0]
        
        answer += sum(numbers[n-1]) - numbers[n-1][0]

        for k in range(n-2, 0, -1):
            answer += numbers[k][k]
        
        print(f"Case #{i}:{answer}")
    
    else:
        break