pibonacci = [1, 1]

for i in range(9998):
    pibonacci.append(pibonacci[-2] + pibonacci[-1])

for cnt in range(1, int(input())+1):
    p, q = map(int, input().split())
    answer = pibonacci[p-1] % q
    print(f'Case #{cnt}: {answer}')