import time

numbers = {}

for i in range(1, 10001):
    numbers[i] = None

for i in range(1, 10001):
    tmp = i
    for j in str(i):
        tmp += int(j)

    if tmp in numbers:
        del numbers[tmp]

print(*numbers, sep='\n')