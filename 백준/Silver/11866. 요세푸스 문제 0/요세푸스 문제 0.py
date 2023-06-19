n, m = map(int, input().split())

people = list(range(1, n+1))
answer = []
array = ''
temp = -1

for _ in range(n):
    temp += m
    while temp >= len(people):
        temp -= len(people)
    answer.append(people[temp])
    people.remove(people[temp])
    temp -= 1

for i in answer:
    array += str(i)
    array += ', '
array = array[:-2:]

print('<' + array + '>')