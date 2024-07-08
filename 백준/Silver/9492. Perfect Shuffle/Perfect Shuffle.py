a, b = [], []
answer = []

while True:
    n = int(input())
    if n != 0:
        a, b = [], []
        answer = []
        if n % 2 == 0:
            for i in range(n):
                if i < n // 2:
                    a.append(input())
                else:
                    b.append(input())
            
            for j in range(n//2):
                answer.append(a[j])
                answer.append(b[j])

            print(*answer, sep="\n")
        
        else:
            for i in range(n):
                if i <= n // 2:
                    a.append(input())
                else:
                    b.append(input())
                
            b.append("")

            for j in range((n//2)+1):
                answer.append(a[j])
                answer.append(b[j])
            
            print(*answer[:-1:], sep="\n")

    else:
        break