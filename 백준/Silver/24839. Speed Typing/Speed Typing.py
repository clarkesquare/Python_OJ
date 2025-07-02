from collections import deque

for cnt in range(1, int(input()) + 1):
    word1 = deque(input())
    word2 = input()
    answer = 0
    for i in range(len(word1)):
        for j in range(len(word2)):
            if word1[i] != word2[j]:
                answer += 1
            
            else:
                break
        
        else:
            answer = 'IMPOSSIBLE'
            break
            
        word2 = word2[j + 1:]

    if answer != 'IMPOSSIBLE':
        if len(word2) != 0:
            answer += len(word2)

    print(f'Case #{cnt}: {answer}')