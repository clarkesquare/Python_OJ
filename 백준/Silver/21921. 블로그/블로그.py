import sys

input = sys.stdin.readline

n, x = map(int, input().split())
prefix_sum = [0]
total = 0
max = 0
pattern = {}

for i in list(map(int, input().split())):
    total += i
    prefix_sum.append(total)

for i in range(n-x+1):
    tmp = prefix_sum[i+x] - prefix_sum[i]
    if tmp not in pattern:
        pattern[tmp] = 1
    
    else:
        pattern[tmp] += 1
    
    if max < tmp:
        max = tmp

if max != 0:
    print(max)
    print(pattern[max])

else:
    print("SAD")