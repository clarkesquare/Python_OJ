pattern = input()

polyomino = ['AAAA', 'BB']

pattern = pattern.replace('XXXX', 'AAAA')
pattern = pattern.replace('XX', 'BB')

if 'X' in pattern:
    print('-1')
else:
    print(pattern)