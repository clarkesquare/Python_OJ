n, m = input().split()
students = []
answer = ''
cnt = 0

for _ in range(int(n)):
    chat = list(input().split())
    students.append(chat)
    if chat[0] == m:
        answer = chat

for i in students[students.index(answer)::-1]:
    if i[1] == answer[1] and i != answer:
        cnt += 1

print(cnt)