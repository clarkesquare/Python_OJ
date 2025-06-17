import sys

input = sys.stdin.readline
answer = [] # 시도한 문제 등
score = {} # 팀 이름: [[푸는 문제들], [이미 푼 문제], 시간]

n, m, q = map(int, input().split())
for i in range(1, n+1):
    score[i] = [{}, {}, 0]

for _ in range(q):
    time, team_num, problem_num, result = input().split()
    time, team_num, problem_num = int(time), int(team_num), int(problem_num)
    if result == 'AC':
        if problem_num not in score[team_num][1]:
            score[team_num][2] += time
            if problem_num in score[team_num][0]:
                score[team_num][2] += score[team_num][0][problem_num] * 20
            
            score[team_num][1][problem_num] = None
    
    else:
        if problem_num not in score[team_num][0]:
            score[team_num][0][problem_num] = 1
        
        else:
            score[team_num][0][problem_num] += 1

for i in score:
    answer.append([i, len(score[i][1]), score[i][2]])

answer.sort(key= lambda x:x[0])
answer.sort(key= lambda x:x[2])
answer.sort(key= lambda x:x[1], reverse=True)

for j in answer:
    print(*j)