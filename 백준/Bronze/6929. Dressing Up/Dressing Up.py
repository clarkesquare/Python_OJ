n = int(input())
pattern = []
tmp = (n - 1) // 2

for i in range(1, tmp+1): # 1, 2, 3, ..., temp + 1
    pattern.append("*" * (i * 2 - 1) + " " * ((tmp + 1 - i) * 4) + "*" * (i * 2 - 1))

pattern.append("*" * (n * 2))

for i in range(tmp, 0, -1):
    pattern.append("*" * (i * 2 - 1) + " " * ((tmp + 1 - i) * 4) + "*" * (i * 2 - 1))

print("\n".join(pattern))