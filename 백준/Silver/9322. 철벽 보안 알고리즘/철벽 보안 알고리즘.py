pattern = {}
words = []
answer_pattern = []
answer = []

for _ in range(int(input())):
    n = int(input())
    words = input().split()
    answer_pattern = [0] * n
    answer = [0] * n
    for i in range(n):
        pattern[words[i]] = i
    
    words = input().split()
    for i in range(n):
        pattern[words[i]] -= i
        answer_pattern[i] = pattern[words[i]]
    
    words = input().split()
    for i in range(n):
        answer[i + answer_pattern[i]] = words[i]
    
    print(*answer)