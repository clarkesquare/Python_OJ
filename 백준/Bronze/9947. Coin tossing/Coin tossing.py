score = [0, 0]

while True:
    n, m = input().split()
    if n != '#' and m != '#':
        score = [0, 0]
        for _ in range(int(input())):
            a, b = input().split()
            if a == b:
                score[0] += 1
            else:
                score[1] += 1
        
        print(n, score[0], m, score[1])
    else:
        break