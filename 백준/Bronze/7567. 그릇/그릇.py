pattern = input()
answer = 10

for i in range(1, len(pattern)):
    if pattern[i] == pattern[i-1]:
        answer += 5
    
    else:
        answer += 10

print(answer)