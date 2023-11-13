problems = []

for _ in range(int(input())):
    n, m = input().split()
    problems.append([n, int(m)])

problems.sort(key=lambda x:x[1])
print(problems[0][0])