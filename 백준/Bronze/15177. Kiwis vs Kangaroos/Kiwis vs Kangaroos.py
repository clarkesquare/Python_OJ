word = input().upper()
KANGAROO, KIWIBIRD = 0, 0

for i in word:
    if i in "KANGAROO":
        KANGAROO += "KANGAROO".count(i)
    if i in "KIWIBIRD":
        KIWIBIRD += "KIWIBIRD".count(i)

if KANGAROO > KIWIBIRD:
    print("Kangaroos")
elif KANGAROO < KIWIBIRD:
    print("Kiwis")
else:
    print("Feud continues")