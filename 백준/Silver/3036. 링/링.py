def lcm(a):
    b = numbers[0]
    a, b = max(a, b), min(a, b)
    while b != 0:
        a, b = b, a % b

    return a

n = int(input())
numbers = list(map(int, input().split()))
answer = []

for i in numbers[1::]:
    answer.append(str(numbers[0]//lcm(i))+'/'+str(i//lcm(i)))

for j in answer:
    print(j)