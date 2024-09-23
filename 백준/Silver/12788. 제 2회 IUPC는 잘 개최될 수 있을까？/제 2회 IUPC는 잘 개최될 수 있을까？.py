n = int(input())
a, b = map(int, input().split())
tmp = a*b
numbers = list(map(int, input().split()))
answer = 0

numbers.sort(reverse=True)
for i in range(n):
    answer += numbers[i]
    if answer >= tmp:
        print(i+1)
        break

else:
    print("STRESS")