drinks = {}
answer = 'Not Delicious...'
alcohol = []

for _ in range(int(input())):
    a, b = input().split()
    b = int(b)
    if a not in drinks:
        drinks[a] = b
    
    else:
        drinks[a] += b

alcohol = sorted(list(drinks.items()), key = lambda x:x[1])
for i in range(len(alcohol) - 1):
    for j in range(1, len(alcohol)):
        if int(alcohol[i][1] * 1.618) == alcohol[j][1]:
            answer = 'Delicious!'
            break
    
    if answer == 'Delicious!':
        break

print(answer)