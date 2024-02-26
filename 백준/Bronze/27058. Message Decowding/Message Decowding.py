from string import ascii_lowercase

alphabets_original = list(ascii_lowercase)
alphabets_new = list(input())

words = input()
answer = ''

for i in words:
    if i.isalpha():
        if i.isupper():
            answer += alphabets_new[alphabets_original.index(i.lower())].upper()
        else:
            answer += alphabets_new[alphabets_original.index(i)]
    
    else:
        answer += i

print(answer)