answer = []

for i in range(1, int(input())+1):
    pattern = list(map(int, input().split()))
    if pattern == [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]:
        answer.append(i)

for j in answer:
    print(j)