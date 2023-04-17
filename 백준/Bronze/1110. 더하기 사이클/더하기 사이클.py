n = input()
original = int(n)
count = 0

while True:
    count += 1
    if len(n) == 1:
        n = str(0) + (n)
    new = int(str(n[-1]) + str(int(n[0]) + int(n[-1]))[-1])
    n = str(new)
    if new == original:
        break

print(count)