bunnies = [1, 1]

for _ in range(int(input())):
    number = int(input())
    bunnies = [1, 1]
    if number == 0 or number == 1:
        print(1)
    else:
        for _ in range(number-1):
            bunnies.append(bunnies[-2] + bunnies[-1])
        
        print(bunnies[-1])