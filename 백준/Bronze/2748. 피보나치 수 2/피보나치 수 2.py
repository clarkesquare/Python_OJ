fibonacci = [0, 1]

for _ in range(int(input())-1):
    fibonacci.append(fibonacci[-2]+fibonacci[-1])

print(fibonacci[-1])