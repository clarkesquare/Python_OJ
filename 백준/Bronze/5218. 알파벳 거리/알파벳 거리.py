alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for _ in range(int(input())):
    answer = []
    words = list(input().split())
    for i in range(len(words[0])):
        temp = alphabets.index(words[1][i]) - alphabets.index(words[0][i])
        answer.append(temp if temp >= 0 else temp+26)
        
    print('Distances:', *answer)