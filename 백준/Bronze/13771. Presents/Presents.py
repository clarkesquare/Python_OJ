prices = []

for _ in range(int(input())):
    prices.append(float(input()))

prices = sorted(prices)
print(f'{prices[1]:.2f}')