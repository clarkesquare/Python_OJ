nums = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4, 'F': 3, 'G': 1, 'H': 3, 'I':1, 'J': 1, 'K': 3, 'L': 1,
        'M': 3, 'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X': 2,
        'Y': 2, 'Z': 1}

n, m = map(int, input().split())
a, b = input().split()
answer = []

if n > m:
    b += ' ' * (n-m)

else:
    a += ' ' * (m-n)

for i in range(max(n, m)):
    if a[i] != ' ':
        answer.append(nums[a[i]])
    
    if b[i] != ' ':
        answer.append(nums[b[i]])

while len(answer) != 2:
    tmp = []
    for i in range(len(answer) - 1):
        tmp.append(int(str(answer[i] + answer[i+1])[-1]))
    
    answer = tmp

if answer[0] == 0:
    answer[0] = ''
    
print(*answer, '%', sep='')