a, b = map(int, input().split())
numbers = []
lunchbox = 0
cnt = 0

for _ in range(b):
    numbers.append(int(input()))

numbers.sort()

while lunchbox < a and cnt < b:
    if lunchbox + numbers[cnt] <= a:
        cnt += 1
        lunchbox += numbers[cnt - 1]

    else:
        break

print(cnt)