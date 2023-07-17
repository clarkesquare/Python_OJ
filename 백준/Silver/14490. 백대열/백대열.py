n, m = map(int, input().split(':'))

a, b = max(n, m), min(n, m)
while b != 0:
    a, b = b, a%b

print(str(n//a)+':'+str(m//a))