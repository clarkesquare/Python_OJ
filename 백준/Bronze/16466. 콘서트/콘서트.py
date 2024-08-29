n = int(input())

tmp = list(map(int, input().split()))
numbers = {}

for i in tmp:
    numbers[i] = ""

for j in range(1, n+1):
    if j not in numbers:
        break

else:
    j += 1

print(j)