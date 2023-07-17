arr = [1, 1, 1]
answer = 1

n = int(input())

if n > 3:
    for i in range(n-3):
        arr.append(arr[-1] + arr[-3])
    answer = arr[-1]

print(answer)