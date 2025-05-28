from string import ascii_uppercase

alpha = {}
answer = 'NO'

for i in range(26):
    alpha[ascii_uppercase[i]] = i

n = int(input())
word = input()
chk = alpha[word[0]]
streak = 0

for i in word[1:]:
    if chk == 0 or chk == 25:
        if chk == 0:
            if alpha[i] == 1:
                streak += 1
            
            else:
                streak = 0
        
        else:
            if alpha[i] == 24:
                streak += 1
            
            else:
                streak = 0

    else:
        if alpha[i] == chk + 1:
            streak += 1
        
        elif alpha[i] == chk - 1:
            streak += 1

        else:
            streak = 0
    
    if streak == 4:
        answer = 'YES'
    
    chk = alpha[i]

print(answer)