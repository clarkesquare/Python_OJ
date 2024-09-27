numbers = {"**** ** ** ****": "0", "  *  *  *  *  *": "1", "***  *****  ***": "2", "***  ****  ****": "3",
           "* ** ****  *  *": "4", "****  ***  ****": "5", "****  **** ****": "6", "***  *  *  *  *": "7",
           "**** ***** ****": "8", "**** ****  ****": "9"}

pattern = []
tmp = ""
answer = ""

for _ in range(5):
    pattern.append(input())

for j in range(0, len(pattern[0]), 4):
    tmp = ""

    for i in range(5):
        tmp += pattern[i][j:j+3]
    
    if tmp in numbers:
        answer += numbers[tmp]
    
    else:
        answer = "BOOM!!"
        break
    
if answer == "BOOM!!" or int(answer) % 6 != 0:
    print("BOOM!!")

else:
    print("BEER!!")