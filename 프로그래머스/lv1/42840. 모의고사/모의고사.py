def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    answer = []
    
    for i in range(len(answers)):
        if student1[i % len(student1)] == answers[i]:
            score[0] = score[0] + 1
        if student2[i % len(student2)] == answers[i]:
            score[1] = score[1] + 1
        if student3[i % len(student3)] == answers[i]:
            score[2] = score[2] + 1
    
    for j in range(3):
        if score[j] == max(score):
            answer.append(j+1)

    return answer