n = int(input())
pattern = input()
stack, answer = 0, 0

for i in range(n):
    if pattern[i] == 'O':
        answer += i+1 + stack
        stack += 1
    else:
        stack = 0

print(answer)