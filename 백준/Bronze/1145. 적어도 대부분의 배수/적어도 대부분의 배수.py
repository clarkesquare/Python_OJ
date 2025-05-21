answer = 0

numbers = list(map(int, input().split()))
numbers.sort()
answer = numbers[2] - 1
chk = 0

while chk == 0:
    answer += 1
    for i in range(5):
        if answer % numbers[i] == 0:
            chk += 1

    if chk >= 3:
        break
    
    chk = 0

print(answer)