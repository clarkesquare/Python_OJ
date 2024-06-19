word_before = []
word_after = []
answer = ""

for _ in range(int(input())):
    a, b = input().split(" = ")
    word_before.append(a)
    word_after.append(b)

for _ in range(int(input())):
    n = int(input())
    answer = list(input().split())
    for i in range(n):
        if answer[i] in word_before:
            answer[i] = word_after[word_before.index(answer[i])]
    
    print(*answer)