a, b = input().split()
word = ""

for i in range(min(len(a), len(b))):
    if i % 2 == 0:
        word += a[i]
    else:
        word += b[i]

print(word)