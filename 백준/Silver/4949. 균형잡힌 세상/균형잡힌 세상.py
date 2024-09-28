word = ""
answer = ""
pattern = ["()", "[]"]

while True:
    word = input()
    if word != ".":
        answer = "yes"
        tmp = ""
        for i in word:
            if i == "(" or i == ")" or i == "[" or i == "]":
                tmp += i

        while len(tmp) != 0:
            if "()" in tmp or "[]" in tmp:
                if "()" in tmp:
                    tmp = tmp.replace("()", "")
                
                else:
                    tmp = tmp.replace("[]", "")

            else:
                answer = "no"
                break
        
        print(answer)

    else:
        break