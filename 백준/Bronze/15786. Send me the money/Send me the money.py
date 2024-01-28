n, m = map(int, input().split())
password = input()

for _ in range(m):
    pattern = input()
    temp = list(password)
    for i in pattern:
        if i == temp[0]:
            del temp[0]
        
        if len(temp) == 0:
            print('true')
            break

    else:
        print('false')