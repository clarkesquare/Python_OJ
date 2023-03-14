a = int(input())
b = int(input())
c = int(input())
total = str(a*b*c)

for i in range(0, 10):
    number = str(i)
    print(total.count(number))