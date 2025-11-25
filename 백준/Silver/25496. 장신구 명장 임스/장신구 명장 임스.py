p, n = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
check = 0

for i in range(n):
    if p < 200:
        p += numbers[i]
        check += 1
    
    else:
        break

print(check)