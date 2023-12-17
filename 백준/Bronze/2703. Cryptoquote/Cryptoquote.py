from string import ascii_uppercase

alphabets = list(ascii_uppercase)
pattern = []
temp = ''
answer = ''

for _ in range(int(input())):
    temp = input()
    answer = ''
    pattern = list(input())
    for i in temp:
        answer += pattern[alphabets.index(i)] if i != ' ' else i

    print(answer)