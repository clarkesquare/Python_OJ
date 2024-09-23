cnt = 0
cnt_input = 0

while True:
    word = input()
    if "-" not in word:
        cnt += 1
        cnt_input = 0
        while True:
            while "{}" in word:
                word = word.replace("{}", "")
            
            if len(word) == 0:
                break

            if word[0] == "}":
                word = "{" + word[1:]
                cnt_input += 1
            
            else:
                for i in range(1, len(word)):
                    if word[i] == "{":
                        word = word[:i] + "}" + word[i+1:]
                        cnt_input += 1
                        break

        print(f"{cnt}. {cnt_input}")
    
    else:
        break