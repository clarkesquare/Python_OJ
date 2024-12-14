from string import ascii_lowercase

answer = {}
for i in ascii_lowercase:
    answer[i] = 0

for i in input():
    answer[i] += 1

for k, v in answer.items():
    print(v, end = " ")