tmp = 0

numbers = list(map(int, input().split()))
answer = 'none'
score = [100, 100, 200, 200, 300, 300, 400, 400, 500]
total = 0

for i in range(len(numbers)):
    if numbers[i] > score[i]:
        answer = 'hacker'
        break
    
    total += numbers[i]

if total >= 100 and answer != 'hacker':
    answer = 'draw'
    
print(answer)
