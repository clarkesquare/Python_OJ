n, m = map(str, input().split())

print(int(str(int(n[-1::-1]) + int(m[-1::-1]))[-1::-1]))