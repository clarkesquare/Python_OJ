e, s, m = map(int, input().split())
answer, a, b, c = 1, 1, 1, 1

while not (e == a and s == b and m == c):
    answer, a, b, c = answer+1, a+1, b+1, c+1
    if a % 16 == 0:
        a = 1
    if b % 29 == 0:
        b = 1
    if c % 20 == 0:
        c = 1

print(answer)