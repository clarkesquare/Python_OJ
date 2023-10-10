pattern_lower = []
pattern_upper = []
word = ''

for _ in range(int(input())):
    n, m = input().split()
    pattern_lower.append(n)
    pattern_upper.append(m)

word = input()

for i in pattern_upper:
    word = word.replace(i, pattern_lower[pattern_upper.index(i)])

a, b = map(int, input().split())

print(word[a-1:b])