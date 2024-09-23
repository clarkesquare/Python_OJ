word = input()
tmp = ""
answer = ""
release = 0

for i in word:
    if i == "<":
        if len(tmp) == 0:  
            tmp = "<"
        
        else:
            answer += tmp[::-1]
            tmp = "<"
        
        release = 1
    
    elif release == 1 and i != ">":
        tmp += i
    
    elif release == 1 and i == ">":
        answer += tmp + ">"
        tmp = ""
        release = 0
    
    elif len(tmp) == 0 or (release == 0 and i != " "):
        tmp += i
    
    elif release == 0 and i == " ":
        answer += tmp[::-1] + " "
        tmp = ""
    
    elif len(tmp) != 0 and i == "<":
        answer += tmp[::-1]
        tmp = ""
    
if len(tmp) != 0:
    answer += tmp[::-1]

print(answer)