n, m = map(int, input().split())
coin = []
answer = 0

for _ in range(n):
    coin.append(int(input()))

for i in coin[::-1]:
    if m // i > 0:
        answer += m // i
        m %= i

print(answer)