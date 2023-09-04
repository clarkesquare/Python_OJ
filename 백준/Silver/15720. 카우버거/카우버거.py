a, b, c = map(int, input().split())
burgers = list(map(int, input().split()))
sides = list(map(int, input().split()))
drinks = list(map(int, input().split()))
price, dc_price = sum(burgers+sides+drinks), 0

for _ in range(min(a, b, c)):
    dc_price += int((max(burgers)+max(sides)+max(drinks))*0.9)
    burgers.remove(max(burgers))
    sides.remove(max(sides))
    drinks.remove(max(drinks))

dc_price += sum(burgers+sides+drinks)
print(price)
print(dc_price)