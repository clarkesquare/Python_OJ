import sys

input = sys.stdin.readline
n, m = map(int, input().split())

subjects = {}
fruits = {}
colors = {}
check = {}

for _ in range(n):
    a, b, c = input().split()
    subjects[a] = None
    fruits[b] = None
    colors[c] = None
    if (a, b, c) not in check:
        check[(a, b, c)] = 1
    
    else:
        check[(a, b, c)] += 1

for _ in range(m):
    answer = 0
    questions = input().strip('\n').split()
    if '-' in questions:
        tmp = [questions]
        tmp2 = []
        for i in range(3):
            tmp2 = []
            for j in range(len(tmp)):
                if tmp[j][i] == '-':
                    if i == 0:
                        for k in subjects:
                            tmp2.append((k, tmp[j][1], tmp[j][2]))
                    
                    elif i == 1:
                        for k in fruits:
                            tmp2.append((tmp[j][0], k, tmp[j][2]))
                    
                    else:
                        for k in colors:
                            tmp2.append((tmp[j][0], tmp[j][1], k))
                
                else:
                    tmp2.append(tmp[j])

            tmp = tmp2
        
        for i in tmp:
            if i in check:
                answer += check[i]
    
    else:
        if tuple(questions) in check:
            answer = check[tuple(questions)]

    print(answer)