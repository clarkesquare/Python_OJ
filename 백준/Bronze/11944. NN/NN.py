n, m = input().split()
m = int(m)

answer = (n * int(n))
if len(answer) >= m:
    print(answer[:m])

else:
    print(answer)