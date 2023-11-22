number1, number2 = input().split()
answer = []

if len(number1) > len(number2):
    number2 = '0' * (len(number1) - len(number2)) + number2
elif len(number1) < len(number2):
    number1 = '0' * (len(number2) - len(number1)) + number1

for i in range(len(number1)):
    answer.append(int(number1[i]) + int(number2[i]))

print(*answer, sep='')