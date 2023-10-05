n = 0

while True:
    n += 1
    a = input()
    b = input()
    if a == b and a == 'END':
        break
    
    a = sorted(a)
    b = sorted(b)
    print('Case', str(n)+':', 'same' if a == b else 'different')