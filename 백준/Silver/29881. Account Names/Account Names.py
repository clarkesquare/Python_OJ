pattern = {}
answer = {}

for _ in range(int(input()) * 2):
    a, b = input().split()
    if a not in pattern:
        pattern[a] = b
    
    else:
        answer[a] = pattern[a], b

for k, v in answer.items():
    print(k, v)