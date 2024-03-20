problems = []
penalty = []
answer = 0
score = 0

while True:
    pattern = input()
    if pattern != '-1':
        a, b, c = pattern.split()
        a = int(a)
        if c == 'right':
            if b in problems:
                score += int(a) + int(penalty[problems.index(b)]) * 20
                penalty[problems.index(b)] = 0

            else:
                score += int(a)

            answer += 1
        
        else:
            if b in problems:
                penalty[problems.index(b)] += 1
            
            else:
                problems.append(b)
                penalty.append(1)
    
    else:
        break

print(answer, score)