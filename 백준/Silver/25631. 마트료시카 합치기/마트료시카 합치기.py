n = int(input())
numbers = list(map(int, input().split()))
answer = []
pattern = {}

for i in numbers:
    if i not in pattern:
        pattern[i] = 1
    
    else:
        pattern[i] += 1

for k, v in pattern.items():
    answer.append([k, v])
    
answer.sort(key= lambda x:x[1], reverse=True)
print(answer[0][1])