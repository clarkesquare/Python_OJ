numbers = list([0] * 10)

for i in input():
    if i == '6':
        numbers[9] = numbers[9] + 1
    else:
        numbers[int(i)] = numbers[int(i)] + 1

numbers[9] = numbers[9]//2 + numbers[9]%2

print(max(numbers))