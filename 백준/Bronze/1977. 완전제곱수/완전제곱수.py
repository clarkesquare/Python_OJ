n = int(input())
m = int(input())
total = 0
min = 0

for i in range(n, m+1):
    number = i ** 0.5
    if int(number) == number:
        total += i
        if min == 0:
            min = i

if not total == 0:
    print(total)
    print(min)
else:
    print("-1")