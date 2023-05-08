game = int(input())
lists = []

for _ in range(game):
    n = int(input())
    a = 0
    lists = list('N' * n)
    while a != n:
        a += 1
        for i in range(a-1, n, a):
            if lists[i] == 'Y':
                lists[i] = 'N'
            else:
                lists[i] = 'Y'

    print(lists.count('Y'))