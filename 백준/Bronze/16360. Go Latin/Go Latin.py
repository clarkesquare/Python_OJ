pattern = {"a": "as", "i": "ios", "y": "ios", "l": "les", "n": "anes", "ne": "anes", "o": "os", "r": "res", "t": "tas", "u": "us", "v": "ves", "w": "was"}

for _ in range(int(input())):
    word = input()
    if word[-1] in pattern:
        word = word[:-1:] + pattern[word[-1]]
    
    elif word[-2:] in pattern:
        word = word[:-2:] + pattern[word[-2:]]
    
    else:
        word += "us"
    
    print(word)