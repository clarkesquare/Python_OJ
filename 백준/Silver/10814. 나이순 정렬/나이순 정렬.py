n = int(input())
people = []

for i in range(n):
    people.append(list(map(str, input().split())))
    people[i][0] = int(people[i][0])

people.sort(key=lambda x: x[0])

for i in people:
    print(i[0], i[1])