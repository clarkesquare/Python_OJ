temp = list(input())
answer = ''

temp.sort(reverse=True)
for i in temp:
    answer += i

print(answer)