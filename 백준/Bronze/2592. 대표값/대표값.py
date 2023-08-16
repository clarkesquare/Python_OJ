numbers = []
cnt, mode = 0, 0

for _ in range(10):
    numbers.append(int(input()))

for i in numbers:
    if numbers.count(i) > cnt:
        cnt = numbers.count(i)
        mode = i

print(int(sum(numbers)/10))
print(mode)