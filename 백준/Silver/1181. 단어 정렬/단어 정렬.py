n = int(input())
temp = []

for _ in range(n):
    word = input()
    if word not in temp:
        temp.append(word)

temp.sort()
temp.sort(key=len)

for i in temp:
    print(i)