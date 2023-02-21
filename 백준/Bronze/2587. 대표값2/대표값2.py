numbers = []
total = 0

for i in range(5):
    numbers.append(int(input()))
    total += numbers[i]

numbers.sort()
print(int(total/len(numbers)))
print(numbers[2])