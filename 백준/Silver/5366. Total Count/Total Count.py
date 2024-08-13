pattern = {}
cnt = 0

while True:
    n = input()
    if n != "0":
        cnt += 1
        if n not in pattern:
            pattern[n] = 1
        else:
            pattern[n] += 1

    else:
        break

for i in pattern:
    print(f"{i}: {pattern[i]}")

print("Grand Total:", cnt)