main = []
temp = []
answer = 0

while True:
    n, m = map(int, input().split())
    if n != 0 and m != 0:
        answer = 0
        main = list(map(int, input().split()))
        for _ in range(m):
            temp = list(map(int, input().split()))
            for i in range(n):
                if main[i] < temp[i]:
                    break
            
            else:
                answer += 1

        print(answer)

    else:
        break