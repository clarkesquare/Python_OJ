from string import ascii_uppercase
import sys

input = sys.stdin.readline
alphabets = {}
alpha = list(ascii_uppercase)
for i in range(26):
    alphabets[alpha[i]] = i

n, q = map(int, input().split())
s = list(input().strip('\n'))

for _ in range(q):
    a, l, r = map(int, input().split())
    l -= 1
    if a == 1:
        cnt = 1
        tmp = s[l]
        for i in range(l + 1, r):
            if tmp != s[i]:
                tmp = s[i]
                cnt += 1
        
        print(cnt)
    
    else:
        for i in range(l, r):
            s[i] = alpha[(alphabets[s[i]] + 1) % 26]