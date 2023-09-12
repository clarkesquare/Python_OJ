stu_a = ['A', 'B', 'C']
stu_b = ['B', 'A', 'B', 'C']
stu_c = ['C', 'C', 'A', 'A', 'B', 'B']
stu_a_score, stu_b_score, stu_c_score, = 0, 0, 0
score, result = 0, 0
answer = []

n = int(input())
test = input()

for i in range(len(test)):
    if stu_a[i % len(stu_a)] == test[i]:
        stu_a_score += 1
    if stu_b[i % len(stu_b)] == test[i]:
        stu_b_score += 1
    if stu_c[i % len(stu_c)] == test[i]:
        stu_c_score += 1
        
score = max(stu_a_score, stu_b_score, stu_c_score)
print(score)

if stu_a_score == score:
    answer.append('Adrian')
if stu_b_score == score:
    answer.append('Bruno')
if stu_c_score == score:
    answer.append('Goran')

for i in answer:
    print(i)