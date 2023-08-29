cnt = 0

while True:
    n = int(input())
    cnt += 1
    students, check = [], []
    earrings = ''

    if n != 0:
        for _ in range(n): # 학생 수만큼 검사
            students.append(input())
            
        for _ in range((n*2)-1): # 학생 수의 2배의 -1번 검사
            earrings = input().split()
            check.append(earrings[0]) if earrings[0] not in check else check.remove(earrings[0])
        
        print(cnt, students[int(check[0])-1])

    else:
        break # 0을 넣으면 while문 종료