n, m, l = map(int, input().split())
pattern = [0] * n
ball = 0

while True:
    if pattern[ball] == m-1:
        break
    pattern[ball] += 1
    
    if pattern[ball] % 2 == 1:
        ball += l
        if ball > n-1:
            ball -= n
    else:
        ball -= l
        if ball < 0:
            ball += n

print(sum(pattern))