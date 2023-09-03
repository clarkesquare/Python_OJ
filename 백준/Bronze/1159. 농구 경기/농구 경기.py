players, answer = [], []

for _ in range(int(input())):
    n = input()[0]
    players.append(n)
    if players.count(n) == 5 and n not in answer:
        answer.append(n)

if len(answer) != 0:
    answer.sort()
    for i in answer:
        print(i, end='')
else:
    print('PREDAJA')