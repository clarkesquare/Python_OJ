recharge = 1000 - int(input())
count = 0
bills = [500, 100, 50, 10, 5, 1]

for i in bills:
    if recharge >= i:
        count += recharge // i
        recharge %= i

print(count)