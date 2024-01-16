n, m = map(int, input().split())
max = n

for i in range(1, m+1):
    number = str(n * i)[::-1]
    if int(number) > max:
        max = int(number)

print(max)