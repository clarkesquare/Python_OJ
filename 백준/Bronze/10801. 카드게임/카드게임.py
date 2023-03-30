list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
score = []

for i in range(10):
    if list_a[i] > list_b[i]:
        score.append('A')
    elif list_a[i] < list_b[i]:
        score.append('B')
    else:
        score.append('D')

if score.count('A') > score.count('B'):
    print('A')
elif score.count('A') < score.count('B'):
    print('B')
else:
    print('D')