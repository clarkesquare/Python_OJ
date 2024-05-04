n = int(input())
pulley = [0] * n
answer = 0
for _ in range(n-1):
    a, b, c = map(int, input().split())
    pulley[b-1] = c

print("1" if pulley.count(1) % 2 == 1 else "0")