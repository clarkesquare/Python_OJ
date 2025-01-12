n = int(input())
numbers = list(map(int, input().split()))
tmp = [numbers[0]]
answer = 0

for i in range(1, len(numbers)):
    if numbers[i] > tmp[-1]:
        tmp.append(numbers[i])
    
    else:
        if answer < tmp[-1] - tmp[0]:
            answer = tmp[-1] - tmp[0]

        tmp = [numbers[i]]

if answer < tmp[-1] - tmp[0]:
    answer = tmp[-1] - tmp[0]

print(answer)