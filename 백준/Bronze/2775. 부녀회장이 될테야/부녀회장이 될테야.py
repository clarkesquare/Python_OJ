apartment = [list(range(1, 15))]
tmp = []
for i in range(0, 14):
    tmp = []
    for j in range(1, 15):
        tmp.append(sum(apartment[i][:j]))
    
    apartment.append(tmp)

for _ in range(int(input())):
    a = int(input())
    b = int(input())
    print(apartment[a][b-1])