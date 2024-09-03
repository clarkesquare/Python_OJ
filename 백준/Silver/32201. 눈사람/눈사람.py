n = int(input())
pattern = {}

numbers = list(input().split())
answer = []
max = 0

for i in range(1, n+1):
    pattern[numbers[i-1]] = i

numbers_new = list(input().split())

for j in range(1, n+1):
    pattern[numbers_new[j-1]] -= j

for k, v in pattern.items():
    answer.append([k, v])
    if v > max:
        max = v

for i in answer:
    if i[1] == max:
        print(i[0], end=" ")