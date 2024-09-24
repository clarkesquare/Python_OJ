while True:
    printline = input()
    answer = "Legal"
    if printline != "#":
        word = ""
        for i in printline:
            if i == "(" or i == "{" or i == "[":
                word += i
            
            elif i == ")" or i == "]" or i == "}":
                if len(word) != 0:
                    if i == ")":
                        if word[-1] == "(":
                            word = word[:-1]
                        
                        else:
                            break
                    
                    elif i == "]":
                        if word[-1] == "[":
                            word = word[:-1]
                        
                        else:
                            break
                    
                    else:
                        if word[-1] == "{":
                            word = word[:-1]
                        
                        else:
                            break
                
                else:
                    word += i
                    break
        
        if len(word) != 0:
            answer = "Illegal"

        print(answer)
    
    else:
        break