pizza = []
answer = 0

for _ in range(8):
    pizza.append(int(input()))

pizza += pizza[:3:]

for i in range(8):
    if sum(pizza[i:i+4]) > answer:
        answer = sum(pizza[i:i+4])

print(answer)