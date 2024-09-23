pattern = {"@": "a", "[": "c", "!": "i", ";": "j", "^": "n", "0": "o", "7": "t"}
cnt = 0

for _ in range(int(input())):
    word = input()
    cnt = 0

    if "\\\\'" in word:
        cnt += word.count("\\\\'")
        word = word.replace("\\\\'", "w")

    if "\\'" in word:
        cnt += word.count("\\'")
        word = word.replace("\\'", "v")
    
    for i in word:
        if i in pattern:
            cnt += word.count(i)
            word = word.replace(i, pattern[i])
    
    if cnt >= len(word) / 2:
        print("I don't understand")
    
    else:
        print(word)