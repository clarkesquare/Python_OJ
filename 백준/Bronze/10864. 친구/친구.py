n, m = map(int, input().split())
friends = [0] * n
a, b = 0, 0

for _ in range(m):
    a, b = map(int, input().split())
    friends[a-1] += 1
    friends[b-1] += 1

for i in friends:
    print(i)