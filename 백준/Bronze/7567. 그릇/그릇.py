plates = input()
total = 0

for i in range(len(plates)):
    if total == 0:
        total += 10
    else:
        if plates[i-1] == plates[i]:
            total += 5
        else:
            total += 10

print(total)