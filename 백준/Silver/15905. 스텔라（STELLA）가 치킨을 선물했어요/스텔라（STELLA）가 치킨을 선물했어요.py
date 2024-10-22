numbers = []
tmp = []
answer = 0

for _ in range(int(input())):
    numbers.append(list(map(int, input().split())))

numbers.sort(key= lambda x:x[1])
numbers.sort(key= lambda x:x[0], reverse=True)
tmp = numbers[4][0]

if len(numbers) >= 6:
    for i in numbers[5:]:
        if i[0] != tmp:
            break
        
        else:
            answer += 1

print(answer)