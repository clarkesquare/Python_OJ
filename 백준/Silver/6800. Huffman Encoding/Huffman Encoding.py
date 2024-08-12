pattern = {}
tmp = ""
answer = ""

for _ in range(int(input())):
    a, b = input().split()
    pattern[b] = a

for i in input():
    tmp += i
    if tmp in pattern:
        answer += pattern[tmp]
        tmp = ""

print(answer)