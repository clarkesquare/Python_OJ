prize2017 = [5000000, 3000000, 2000000, 500000, 300000, 100000]
prize2018 = [5120000, 2560000, 1280000, 640000, 320000]

for _ in range(int(input())):
    answer = 0
    n, m = map(int, input().split())
    if n != 0:
        if n == 1:
            answer += prize2017[0]
        elif n <= 3:
            answer += prize2017[1]
        elif n <= 6:
            answer += prize2017[2]
        elif n <= 10:
            answer += prize2017[3]
        elif n <= 15:
            answer += prize2017[4]
        elif n <= 21:
            answer += prize2017[5]
    
    if m != 0:
        if m == 1:
            answer += prize2018[0]
        elif m <= 3:
            answer += prize2018[1]
        elif m <= 7:
            answer += prize2018[2]
        elif m <= 15:
            answer += prize2018[3]
        elif m <= 31:
            answer += prize2018[4]
    
    print(answer)