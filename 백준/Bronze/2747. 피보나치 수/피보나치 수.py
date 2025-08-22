fibo = [0, 1]

for _ in range(int(input()) - 1):
    fibo.append(fibo[-2] + fibo[-1])

print(fibo[-1])