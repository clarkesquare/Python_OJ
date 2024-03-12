factorial = 1
for i in range(1, int(input())+1):
    factorial *= i

print(str(factorial).count('0'))