number = int(input())

while True:
    number += 1
    for i in str(number):
        if str(number).count(i) >= 2:
            break
    else:
        print(number)
        break