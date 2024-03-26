fruits = []
numbers = []

for _ in range(int(input())):
    n, m = input().split()
    m = int(m)
    if n in fruits:
        numbers[fruits.index(n)] += m
    else:
        fruits.append(n)
        numbers.append(m)

print("YES" if 5 in numbers else "NO")