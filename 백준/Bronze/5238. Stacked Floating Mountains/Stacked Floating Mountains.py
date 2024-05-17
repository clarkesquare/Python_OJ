numbers = []

for _ in range(int(input())):
    numbers = list(map(int, input().split()))
    tmp = numbers[1]
    for i in range(2, numbers[0]):
        if tmp + numbers[i] != numbers[i+1]:
            print("NO")
            break
            
        tmp = numbers[i]
        
    else:
        print("YES")