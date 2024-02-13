n = int(input())
names = []

for _ in range(n):
    names.append(input())

for i in range(1, n+1):
    print(str(i) + ". " + names[i-1])