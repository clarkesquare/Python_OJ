numbers = [0, 1]

n = int(input())
for i in range(n - 1):
    numbers.append((numbers[-2] + numbers[-1]) % 1000000007)

if n == 0:
    print(0)

else:
    print(numbers[-1])