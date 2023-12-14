a = int(input())
b = int(input())
c = int(input())
temp = str(a*b*c)

for i in range(10):
    print(temp.count(str(i)))