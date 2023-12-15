cola = ''
answer = 0

for _ in range(int(input())):
    answer = 0
    cola = input()
    for i in range(len(cola)):
        answer += int(cola[::-1][i]) * (2 ** i)
    
    print(answer)