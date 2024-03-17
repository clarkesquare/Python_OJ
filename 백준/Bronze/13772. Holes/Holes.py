one_hole = ['A', 'D', 'O', 'P', 'Q', 'R']
word = ''
answer = 0

for _ in range(int(input())):
    word = input()
    answer = 0
    for i in word:
        if i in one_hole:
            answer += 1
        elif i == 'B':
            answer += 2
    
    print(answer)