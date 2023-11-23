n = list(map(int, input()))
numbers = [[], []]
test1, test2 = 1, 1
answer = 'NO'

for i in range(1, len(n)):
    numbers[0], numbers[1] = n[:i], n[i:]
    test1, test2 = 1, 1
    for j in numbers[0]:
        test1 *= int(j)
    
    for k in numbers[1]:
        test2 *= int(k)
    
    if test1 == test2:
        answer = 'YES'
        break

print(answer)