n = int(input())
people = list(map(int, input().split()))
temp, answer = 0, 0

people.sort()
for i in people:
    temp += i
    answer += temp

print(answer)