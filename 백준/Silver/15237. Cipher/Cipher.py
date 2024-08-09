n, m = map(int, input().split())
numbers = map(int, input().split())
pattern = {}
answer = []

for i in numbers:
    if i not in pattern:
        pattern[i] = 1

    else:
        pattern[i] += 1

answer = list(pattern.items())
answer.sort(key= lambda x:x[1], reverse=True)

for j in answer:
    print((str(j[0]) + " ") * j[1], end="")