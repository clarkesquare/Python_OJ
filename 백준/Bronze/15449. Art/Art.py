numbers = list(map(int, input().split()))
answer = 0

numbers.sort()
for i in range(len(numbers)-2):
    for j in range(i+1, len(numbers)-1):
        for k in range(j+1, len(numbers)):
            if numbers[i] + numbers[j] > numbers[k]:
                answer += 1

print(answer)