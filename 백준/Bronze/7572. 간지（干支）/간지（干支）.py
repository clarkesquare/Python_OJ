iji = 'ABCDEFGHIJKL'

n = int(input())

print(iji[(n-4) % 12] + str((n % 10 + 6) % 10))