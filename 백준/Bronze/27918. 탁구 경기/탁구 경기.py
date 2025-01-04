answer = [0, 0]

for _ in range(int(input())):
    game = input()
    if game == 'D':
        answer[0] += 1
    
    else:
        answer[1] += 1

    if abs(answer[0] - answer[1]) == 2:
        break

print(str(answer[0])+':'+str(answer[1]))