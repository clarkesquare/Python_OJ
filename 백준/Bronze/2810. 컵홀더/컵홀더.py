cnt = 0
temp = ['*']
n = int(input())
seats = input()
seats = list(seats.replace('LL', 'L'))

for i in seats:
    if i == 'L':
        i = ['S', 'S']
        temp += i
    else:
        temp.append(i)
    temp.append('*')

for j in range(len(temp)):
    if temp[j] == 'S':
        if temp[j-1] == '*':
            temp[j-1], temp[j] = '?', '?'
            cnt += 1
        elif temp[j+1] == '*':
            temp[j], temp[j+1] = '?', '?'
            cnt += 1

print(cnt)