numbers = []

for _ in range(int(input())):
    numbers.append(int(input()))

if numbers[2] - numbers[1] == numbers[1] - numbers[0]:
    print(numbers[-1] + (numbers[1] - numbers[0]))
else:
    print(int(numbers[-1] * (numbers[1] / numbers[0])))