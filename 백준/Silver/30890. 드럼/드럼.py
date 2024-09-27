a, b = map(int, input().split())

dictionary = {}
answer = []

for i in range(1, a+1):
    dictionary[i/a] = 1

for j in range(1, b+1):
    if j/b in dictionary:
        dictionary[j/b] = 3

    else:
        dictionary[j/b] = 2

for k, v in dictionary.items():
    answer.append([k, v])

answer.sort(key= lambda x:x[0])

for i in answer:
    print(i[1], end="")