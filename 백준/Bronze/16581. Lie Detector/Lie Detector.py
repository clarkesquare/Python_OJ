temp = []
n = int(input())

for _ in range(n):
    temp.append(input())

for i in range(n-1, 0, -1):
    if temp[i] == "LIE":
        temp[i-1] = "LIE" if temp[i-1] == "TRUTH" else "TRUTH"

print(temp[0])