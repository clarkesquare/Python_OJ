from string import ascii_uppercase

alphabets = list(ascii_uppercase)
score = [3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1]
answer = 0

numbers = list(input())
for i in numbers:
    answer += score[alphabets.index(i)]

if answer % 2 != 0:
    print('I\'m a winner!')
else:
    print('You\'re the winner?')