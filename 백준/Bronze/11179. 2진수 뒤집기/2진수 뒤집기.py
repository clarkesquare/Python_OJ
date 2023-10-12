n = int(input())

n = '0b' + bin(n)[2::][::-1]
print(int(n, 2))