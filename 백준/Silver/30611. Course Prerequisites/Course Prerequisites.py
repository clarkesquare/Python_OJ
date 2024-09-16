course = {}
answer = 1

n = int(input())
pattern_before = input().split()
for i in pattern_before:
    course[i] = ""

n = int(input())
pattern_after = input().split()
for i in pattern_after:
    if i in course:
        course.pop(i)
    
    else:
        answer = 0
        break

print(answer)