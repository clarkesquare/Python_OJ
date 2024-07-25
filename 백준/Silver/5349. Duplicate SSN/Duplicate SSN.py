numbers = []
exist = []

while True:
    tmp = input()
    if tmp != "000-00-0000":
        if tmp not in numbers:
            numbers.append(tmp)
        elif tmp not in exist:
            exist.append(tmp)
    
    else:
        break

exist.sort()
print(*exist, end="\n")