n = int(input())
honeycome = 1
cnt = 1

while n > honeycome:
    honeycome += (cnt * 6)
    cnt += 1

print(cnt)