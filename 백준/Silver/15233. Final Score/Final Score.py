a, b, c = map(int, input().split())
scores = [0, 0]

A = set(input().split())
B = set(input().split())
C = input().split()

for i in C:
    if i in A:
        scores[0] += 1
    else:
        scores[1] += 1

if scores[0] > scores[1]:
    print("A")
elif scores[0] < scores[1]:
    print("B")
else:
    print("TIE")