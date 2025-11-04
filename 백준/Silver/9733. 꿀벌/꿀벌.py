import sys

input = sys.stdin.readlines

pattern = {'Re': 0, 'Pt': 0, 'Cc': 0, 'Ea': 0, 'Tb': 0, 'Cm': 0, 'Ex': 0}
tmp = []

works = input()
for i in works:
    tmp += i.strip().split()

for i in range(len(tmp)):
    if tmp[i] in pattern:
        pattern[tmp[i]] = pattern.get(tmp[i], 0) + 1

for k, v in pattern.items():
    print(f'{k} {v} {(v/len(tmp)):.2f}')

print('Total', len(tmp), '1.00')