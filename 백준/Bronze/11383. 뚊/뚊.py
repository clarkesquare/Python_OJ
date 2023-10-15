n, m = map(int, input().split())
test1, test2, temp = '', '', ''

for _ in range(n):
    test1 += input()

for _ in range(n):
    test2 += input()
    
for i in test1:
    temp += i * 2

print('Eyfa' if temp == test2 else 'Not Eyfa')