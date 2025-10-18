n, m = map(int, input().split())
pattern = []
answer_dna = ''
answer = 0

for _ in range(n):
    pattern.append(input())

for i in range(m):
    check = {}
    for j in range(n):
        if pattern[j][i] not in check:
            check[pattern[j][i]] = 1
        
        else:
            check[pattern[j][i]] += 1
    
    check = list(check.items())
    check.sort(key= lambda x:x[0])
    check.sort(key= lambda x:x[1], reverse=True)
    answer_dna += check[0][0]
    for tmp in range(1, len(check)):
        answer += check[tmp][1]

print(answer_dna)
print(answer)