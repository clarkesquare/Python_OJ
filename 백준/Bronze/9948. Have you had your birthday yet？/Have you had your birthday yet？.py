month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


while True:
    d, m = input().split()
    d = int(d)
    if d == 0 or m == "#":
        break
    else:
        if d == 4 and m == month[7]:
            print("Happy birthday")
        elif d == 29 and m == month[1]:
            print("Unlucky")
        elif month.index(m) < 7 or (month.index(m) == 7 and d < 4):
            print("Yes")
        else:
            print("No")