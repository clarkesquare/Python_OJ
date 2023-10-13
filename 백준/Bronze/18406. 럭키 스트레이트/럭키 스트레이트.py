n = list(map(int, input()))
n1, n2 = sum(n[:len(n)//2]), sum(n[len(n)//2::])

print('LUCKY' if n1 == n2 else 'READY')