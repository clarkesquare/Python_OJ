n = int(input())
i = 1
numbers = []

while n != 1:
    i += 1
    if n % i == 0:
        numbers.append(i)
        n //= i
        i = 1

for j in numbers:
    print(j)