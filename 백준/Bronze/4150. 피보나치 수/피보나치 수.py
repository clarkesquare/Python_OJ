fibo = [0, 1]

n = int(input())

for _ in range(n-1):
    fibo.append(fibo[-2] + fibo[-1])

print(fibo[-1])