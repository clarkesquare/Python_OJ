for i in range(int(input())):
    answer = "INSOMNIA"
    n = int(input())
    cnt = 0
    check = {}
    while n != 0:
        cnt += 1
        for j in str(n * cnt):
            if j not in check:
                check[j] = ''
        
        if len(check) == 10:
            answer = n * cnt
            break

    print(f"Case #{i+1}: {answer}")