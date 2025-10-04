from string import ascii_lowercase

dict = {}
for i in range(26):
    dict[ascii_lowercase[i]] = i

word = input()
check = dict[word[0]]
answer = 1
streak = 1

for i in range(1, len(word)):
    if check < dict[word[i]]:
        streak += 1
    
    else:
        streak = 1
    
    answer += streak
    check = dict[word[i]]
    

print(answer)