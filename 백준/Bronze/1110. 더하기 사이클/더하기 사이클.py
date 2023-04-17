n = input()
original = int(n)
count = 0

while True:
    count += 1
    if len(n) == 1:
        n = str(0) + n
    new = int(n[-1] + str(int(n[0]) + int(n[-1]))[-1])
    if new == original:
        break
    n = str(new)

print(count)