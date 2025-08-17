import sys

input = sys.stdin.readline
n, m = map(int, input().split())
bid = {}
low = m + 1
chk = 0

for _ in range(m):
    a, b = input().split()
    b = int(b)
    if b not in bid:
        bid[b] = [a]
    
    else:
        bid[b].append(a)

bid = list(bid.items())
bid.sort(key= lambda x:x[0])

for i in range(len(bid)):
    if len(bid[i][1]) == 1:
        chk = -1
        break
    
    else:
        if len(bid[i][1]) < low:
            low = len(bid[i][1])
            chk = i

if chk != -1:
    print(bid[chk][1][0], bid[chk][0])

else:
    print(*bid[i][1], bid[i][0])