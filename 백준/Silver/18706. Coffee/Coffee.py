coffees = []
costs = []
tmp = []
answer = []
fee = 0

for _ in range(int(input())):
    coffees = []
    costs = []
    tmp = []
    answer = []
    fee = 0
    a, b = map(int, input().split())
    for _ in range(a):
        coffee, s, m, l = input().split()
        s, m, l = int(s), int(m), int(l)
        coffees.append(coffee)
        costs.append([s, m, l])

    for _ in range(b):
        tmp = list(input().split())
        if tmp[1] == "small":
            fee = costs[coffees.index(tmp[2])][0]
        elif tmp[1] == "medium":
            fee = costs[coffees.index(tmp[2])][1]
        else:
            fee = costs[coffees.index(tmp[2])][2]
        
        fee += 100 // b
        if str(fee)[-1] == "4" or str(fee)[-1] == "9":
            fee += 1
        elif str(fee)[-1] == "1" or str(fee)[-1] == "6":
            fee -= 1

        print(tmp[0], fee)