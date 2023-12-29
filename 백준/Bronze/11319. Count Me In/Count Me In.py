vowels = ['a', 'e', 'i', 'o', 'u']
answer = [0, 0]

for _ in range(int(input())):
    word = input().lower()
    answer = [0, 0]
    for i in word:
        if i != ' ':
            answer[0 if i not in vowels else 1] += 1
    
    print(*answer)