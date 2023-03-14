h, m = map(int, input().split())
time = int(input())
temp = 0

temp = (h * 60) + m
temp += time

h = temp // 60
temp -= h * 60
m = temp

if h >= 24:
    h -= 24

print(h, m)