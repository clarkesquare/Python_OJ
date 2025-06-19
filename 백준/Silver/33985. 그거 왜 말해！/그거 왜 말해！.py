n = int(input())
word = input()
answer = 'Yes'

if word[-1] == 'A' and 'B' in word:
    answer = 'No'

elif word[0] == 'B':
    answer = 'No'

elif 'B' not in word:
    answer = 'No'

print(answer)