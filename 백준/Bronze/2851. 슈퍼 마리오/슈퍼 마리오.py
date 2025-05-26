tmp = 0
numbers = []
chk = 0
answer = 1000

for i in range(10):
    tmp += int(input())
    if abs(tmp - 100) <= answer:
        answer = abs(tmp - 100)
        chk = tmp

print(chk)