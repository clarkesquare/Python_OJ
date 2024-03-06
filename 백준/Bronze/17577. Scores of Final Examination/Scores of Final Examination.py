scores = []
temp = []

while True:
    n, m = map(int, input().split())
    if n != 0 and m != 0:
        scores = [0] * n
        for _ in range(m):
            temp = list(map(int, input().split()))
            for i in range(n):
                scores[i] += temp[i]
        
        print(max(scores))

    else:
        break