n, m = map(int, input().split())
answer = []
cnt = 1

while n // cnt >= 1 and m // cnt >= 1:
    if n % cnt == 0 and m % cnt == 0:
        answer.append(cnt)

    cnt += 1

for i in answer:
    print(i, n//i, m//i)