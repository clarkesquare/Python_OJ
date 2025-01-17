from itertools import permutations

for i in range(int(input())):
    word = input()
    pattern = permutations(word)

    print(f"Case # {i + 1}:")
    for j in pattern:
        print(''.join(j))