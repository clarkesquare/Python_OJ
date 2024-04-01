from string import ascii_lowercase
alphabets = list(ascii_lowercase)
temp = 0
word = ''

for _ in range(int(input())):
    n = int(input())
    numbers = list(map(int, input().split()))
    alphabets = list(ascii_lowercase)
    temp = 0
    word = ''
    for i in numbers:
        temp = i
        word += alphabets[temp]
        alphabets = list(alphabets[temp]) + alphabets[:temp:] + alphabets[temp+1::]
    
    print(word)