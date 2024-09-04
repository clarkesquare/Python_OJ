n, m = map(int, input().split())
word = input()
tmp = ""
pattern = {}

for i in range(len(word)-n+1):
    tmp = word[i:i+n]
    if tmp not in pattern:
        pattern[tmp] = ""

print(len(pattern))