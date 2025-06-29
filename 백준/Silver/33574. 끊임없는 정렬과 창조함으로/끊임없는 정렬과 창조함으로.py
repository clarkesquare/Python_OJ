answer = []

for _ in range(int(input())):
    numbers = list(map(int, input().split()))
    if numbers[0] == 1:
        if numbers[1] == 1:
            answer.sort()
        
        else:
            answer.sort(reverse=True)
    
    else:
        answer.insert(numbers[1], numbers[2])

print(len(answer))
print(*answer)