from string import ascii_uppercase

alphabets = {}
numbers = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
tmp = []
answer = []

for i in range(26):
    alphabets[ascii_uppercase[i]] = numbers[i]

name_a = input()
name_b = input()
for i in range(len(name_a)):
    answer.append(alphabets[name_a[i]])
    answer.append(alphabets[name_b[i]])

while len(answer) != 2:
    tmp = []
    for i in range(len(answer) - 1):
        tmp.append(answer[i] + answer[i+1])

    answer = tmp

answer = list(map(str, answer))
for i in answer:
    print(i[-1], end='')