n = int(input())
names = []

for _ in range(n):
    names.append(input())

for i in range(n):
    print(str(i+1) + ". " + names[i])