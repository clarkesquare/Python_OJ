from string import ascii_lowercase

alphabets = list(ascii_lowercase)
new_alphabets = ["@", "8", "(", "|)", "3", "#", "6", "[-]", "|", "_|", "|<", "1", "[]\\/[]", "[]\\[]", "0", "|D", "(,)", "|Z", "$", "']['", "|_|", "\\/", "\\/\\/", "}{", "`/", "2"]

word = input().lower()
answer = ''

for i in word:
    answer += new_alphabets[alphabets.index(i)] if i in alphabets else i

print(answer)