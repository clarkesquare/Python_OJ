numbers = []
lefts = []
cnt = 0

for _ in range(10):
    numbers.append(int(input()))

for i in numbers:
    n = i % 42
    if n not in lefts:
        lefts.append(n)
        cnt += 1

print(cnt)