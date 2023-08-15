pattern = input()

polyomino = ['AAAA', 'BB']

pattern = pattern.replace('XXXX', 'AAAA')
pattern = pattern.replace('XX', 'BB')

print('-1' if 'X' in pattern else pattern)