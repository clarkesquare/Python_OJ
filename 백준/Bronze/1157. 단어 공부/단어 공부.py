from string import ascii_uppercase

alphabets = list(ascii_uppercase)
alphabets_cnt = [0] * 26

word = input().upper()
for i in range(len(alphabets)):
    alphabets_cnt[i] += word.count(alphabets[i])

if alphabets_cnt.count(max(alphabets_cnt)) >= 2:
    print('?')
    
else:
    print(alphabets[alphabets_cnt.index(max(alphabets_cnt))])