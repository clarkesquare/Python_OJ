numbers = set(i for i in range(1, 10))
tmp = set([])
n = int(input())

for _ in range(n-1):
    tmp = set([])
    for i in numbers:
        for j in range(1, 10):
            if i * j not in tmp:
                tmp.add(i*j)

    numbers = numbers|tmp

print(len(numbers))