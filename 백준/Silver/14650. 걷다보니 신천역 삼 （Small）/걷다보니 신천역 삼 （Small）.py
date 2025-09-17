n = int(input())
answer = 0
numbers = ['0', '1', '2']
check = ['']
tmp = []

for _ in range(n):
    tmp = []
    for i in range(len(check)):
        for j in range(3):
            if check[i] + numbers[j] != '0':
                tmp.append(check[i] + numbers[j])

    check = tmp

for num in check:
    if int(num) % 3 == 0:
        answer += 1

print(answer)