n, m = map(int, input().split())
pattern = {}

for _ in range(n):
    a, b = input().split()
    pattern[a] = b

for _ in range(m):
    word = input()
    if word in pattern:
        print(pattern[word])
    
    else:
        if word[-1] == "y" and word[-2] not in ["a", "e", "i", "o", "u"]:
            print(word[:-1:] + "ies")
        
        elif word[-1] in ["o", "s", "x"] or word[-2:] in ["ch", "sh"]:
            print(word + "es")
        
        else:
            print(word + "s")