n = int(input())
temp = ''
answer = ''

if n == 1:
    answer = input()
else:
    for _ in range(n):
        if len(temp) == 0:
            temp = input()
        else:
            answer = ''
            word = input()
            for i in range(len(temp)):
                if temp[i] == word[i]:
                    answer += temp[i]
                else:
                    answer += '?'
            temp = answer

print(answer)