answer = "WHERE IS MY CHICKEN?"

tmp = list(map(int, input().split()))
a, b = map(int, input().split())
if a != tmp[0]:
    gradient = (b - tmp[1]) / (a - tmp[0])
else:
    gradient = 1

tmp = [a, b]

a, b = map(int, input().split())
if a != tmp[0]:
    if gradient != (b - tmp[1]) / (a - tmp[0]):
        answer = "WINNER WINNER CHICKEN DINNER!"

print(answer)