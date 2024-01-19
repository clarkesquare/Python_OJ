candidates = []


for _ in range(int(input())):
    name = input()
    if len(name) == 3:
        candidates.append(name)

candidates.sort()
print(candidates[0])