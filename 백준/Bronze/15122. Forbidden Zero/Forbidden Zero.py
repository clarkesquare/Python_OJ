n = list(str(int(input()) + 1))[::-1]
answer = ''

for i in range(len(n)):
    if n[i] == '0':
        n[i] = '1'
    
    answer += n[i]

print(answer[::-1])