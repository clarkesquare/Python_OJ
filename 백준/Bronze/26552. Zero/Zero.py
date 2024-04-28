for _ in range(int(input())):
    number = int(input())
    while True:
        number += 1
        if "0" not in str(number):
            break
    
    print(number)