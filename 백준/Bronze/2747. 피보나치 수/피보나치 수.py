n = int(input())
a = 0
b = 1

for i in range (n):
    total = a+b
    a = b
    b = total

print(a)