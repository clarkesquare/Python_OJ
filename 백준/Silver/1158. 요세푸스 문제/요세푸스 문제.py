n, k = map(int, input().split())
circle = list(range(1, n+1))
answer = []
i = 0

while len(circle) != 0:
    i += k-1
    if i >= len(circle):
        i %= len(circle)
    answer.append(circle[i])
    del circle[i]

print('<' + ', '.join(list(map(str, answer))) + '>')