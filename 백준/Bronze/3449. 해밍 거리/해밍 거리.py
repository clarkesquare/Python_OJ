for _ in range(int(input())):
    a = input()
    b = input()
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    
    print(f'Hamming distance is {cnt}.')