import string

alphabet = list(string.ascii_lowercase)
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
cnt = 0

for _ in range(int(input())):
    word = ''
    cnt += 1
    pattern = list(input().split())
    for i in pattern:
        word += alphabet[morse.index(i)].upper()
    
    print('Case', str(cnt)+':', word)