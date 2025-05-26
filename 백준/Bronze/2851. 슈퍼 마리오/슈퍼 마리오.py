tmp = 0
numbers = []
chk = 0

for i in range(10):
    tmp += int(input())
    numbers.append(tmp)

answer = 1000

for i in range(10):
    if abs(numbers[i] - 100) <= answer:
        answer = abs(numbers[i] - 100)
        chk = numbers[i]

print(chk)