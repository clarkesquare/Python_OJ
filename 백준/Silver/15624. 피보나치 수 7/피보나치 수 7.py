numbers = [0, 1]

for i in range(int(input()) - 1):
    numbers.append((numbers[-2] + numbers[-1]) % 1000000007)

print(numbers[-1])