n = int(input())

for i in range(n):
    combo = 0
    result = 0
    answer = input()
    for j in answer:
        if j == 'O':
            combo += 1
            result += combo
        else:
            combo = 0
    print(result)