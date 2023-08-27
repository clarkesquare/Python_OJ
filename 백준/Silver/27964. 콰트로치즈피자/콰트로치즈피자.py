n = int(input())
toppings = list(input().split())
pizza = []

for i in toppings:
    if i[-6::] == 'Cheese' and i not in pizza:
        pizza.append(i)

print('yummy' if len(pizza) >= 4 else 'sad')