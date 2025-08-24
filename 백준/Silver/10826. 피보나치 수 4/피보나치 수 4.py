n = int(input())
a, b = 0, 1

if n == 0:
    print(a)

else:
    for _ in range(n-1):
        a, b = b, a + b

    print(b)