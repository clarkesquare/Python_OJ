pattern = ''
words = []
answer = ''
cnt = 0

while True:
    n = int(input())
    pattern = ''
    words = []
    answer = ''
    cnt = 0

    if n != 0:
        pattern = input()
        for i in range(0, len(pattern), n):
            cnt += 1
            if cnt % 2 == 1:
                words.append(pattern[i:i+n:])
            else:
                words.append(pattern[i+n-1:i-1:-1])

        for j in range(n):
            for k in range(len(words)):
                answer += words[k][j]
        
        print(answer)

    else:
        break