a = list(input())
b = list(input())
answer = ["", ""]

if len(a) > len(b):
    b = ["0"] * (len(a) - len(b)) + b

else:
    a = ["0"] * (len(b) - len(a)) + a


for i in range(len(a)):
    if a[i] >= b[i]:
        answer[0] += a[i]

for i in range(len(a)):
    if b[i] >= a[i]:
        answer[1] += b[i]


if len(answer[0]) != 0:
    print(int(answer[0]))

else:
    print("YODA")

if len(answer[1]) != 0:
    print(int(answer[1]))

else:
    print("YODA")