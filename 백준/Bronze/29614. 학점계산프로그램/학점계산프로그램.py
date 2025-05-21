grade = input()
jumsu = {'A+': 4.5, 'A': 4.0, 'B+': 3.5, 'B': 3.0, 'C+': 2.5, 'C': 2.0, 'D+': 1.5, 'D': 1.0, 'F': 0.0}
tmp = ''
score = 0
cnt = 0

for i in range(len(grade)):
    if grade[i] != '+':
        if len(tmp) == 0:
            tmp += grade[i]
        
        else:
            score += jumsu[tmp]
            tmp = grade[i]
            cnt += 1
        
    else:
        tmp += '+'
    
    if i == len(grade) - 1:
        score += jumsu[tmp]
        tmp = ''
        cnt += 1

print(round(score / cnt, 5))