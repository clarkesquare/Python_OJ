from string import ascii_uppercase

answer = 0
numbers = {}
for i in range(len(ascii_uppercase)):
    numbers[ascii_uppercase[i]] = i + 10

a, b = input().split()
b = int(b)

a = a[::-1]
for i in range(len(a)):
    if a[i].isnumeric():
        answer += int(a[i]) * (b ** i)
    
    else:
        answer += numbers[a[i]] * (b ** i)

print(answer)