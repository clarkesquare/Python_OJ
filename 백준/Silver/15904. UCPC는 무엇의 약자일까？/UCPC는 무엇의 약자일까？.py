word = input()
answer = 'hate'
chk = 'UCPC'
num = 0

for i in word:
    if i == chk[num]:
        num += 1
    
    if num == 4:
        answer = 'love'
        break


print(f'I {answer} UCPC')