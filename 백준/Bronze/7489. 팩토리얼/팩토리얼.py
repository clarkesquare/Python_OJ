answer = 1

for _ in range(int(input())):
    answer = 1
    for i in range(1, int(input())+1):
        answer *= i

    for j in str(answer)[::-1]:
        if j != '0':
            print(j)
            break