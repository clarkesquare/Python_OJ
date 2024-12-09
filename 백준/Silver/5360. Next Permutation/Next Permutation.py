from itertools import permutations

for _ in range(int(input())):
    number = input()
    numbers = list(map("".join, permutations(sorted(number), len(number))))

    if numbers[-1] == number:
        print("USELESS")
    
    else:
        for i in range(len(numbers) - 1, -1, -1):
            if numbers[i] == number:
                print(numbers[i+1])
                break