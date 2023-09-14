pattern_a = input()
pattern_b = input()
pattern, temp = '', ''

for i in range(len(pattern_a)):
    pattern += pattern_a[i] + pattern_b[i]

while len(pattern) != 2:
    temp = ''
    for i in range(1, len(pattern)):
        temp += str(int(pattern[i])+int(pattern[i-1]))[-1]
    
    pattern = temp

print(pattern)