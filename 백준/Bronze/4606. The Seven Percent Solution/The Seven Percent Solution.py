before = ['%', ' ', '!', '$', '(', ')', '*']
after = ['%25', '%20', '%21', '%24', '%28', '%29', '%2a']

while True:
    word = input()
    if word == '#':
        break
    else:
        for i in range(len(before)):
            word = word.replace(before[i], after[i])
    
    print(word)