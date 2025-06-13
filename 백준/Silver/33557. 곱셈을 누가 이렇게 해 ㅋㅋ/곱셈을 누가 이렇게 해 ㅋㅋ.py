for _ in range(int(input())):
    a, b = input().split()
    chk1 = int(a) * int(b)
    chk2 = ''
    length = max(len(a), len(b)) - min(len(a), len(b))
    if len(a) > len(b):
        b = '1' * length + b
    
    else:
        a = '1' * length + a

    for i in range(len(a)):
        chk2 += str(int(a[i]) * int(b[i]))

    chk2 = int(chk2)
    if chk1 == chk2:
        print(1)
    
    else:
        print(0)