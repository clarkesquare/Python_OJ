word = input()
pattern = {'P': 0, 'K': 0}
pattern[word[0]] += 1

for i in range(1, len(word)):
    if word[i] == 'K':
        if pattern['P'] >= 1:
            pattern['P'] -= 1
            pattern['K'] += 1
        
        else:
            pattern['K'] += 1
    
    else:
        if pattern['K'] >= 1:
            pattern['P'] += 1
            pattern['K'] -= 1
        
        else:
            pattern['P'] += 1

print(pattern['P'] + pattern['K'])