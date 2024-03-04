requires = [0, 0, 0, 0] # 소문자, 대문자, 숫자, 심볼
symbol = '+_)(*&^%$#@!./,;{}'
n = 0
testcase = ''

for _ in range(int(input())):
    n = int(input())
    testcase = input()
    requires = [0, 0, 0, 0]
    if n < 12:
        print("invalid")
    else:
        for i in testcase:
            if i.islower() and requires[0] == 0:
                requires[0] = 1
            elif i.isupper() and requires[1] == 0:
                requires[1] = 1
            elif i.isdigit() and requires[2] == 0:
                requires[2] = 1
            elif i in symbol and requires[3] == 0:
                requires[3] = 1
        
        if 0 in requires:
            print("invalid")
        else:
            print("valid")