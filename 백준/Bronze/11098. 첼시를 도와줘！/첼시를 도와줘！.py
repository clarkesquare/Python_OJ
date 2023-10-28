for _ in range(int(input())):
    answer = [0, '']
    max = 0
    for _ in range(int(input())):
        n, m = input().split()
        n = int(n)
        if n > answer[0]:
            answer[0], answer[1] = n, m
            
    print(answer[1])