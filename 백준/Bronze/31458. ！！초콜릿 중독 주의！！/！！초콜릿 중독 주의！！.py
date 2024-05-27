for _ in range(int(input())):
    tmp = []
    pattern = input()
    answer = 0
    if "0" in pattern:
        answer = 0
        tmp = pattern.split("0")
    else:
        answer = 1
        tmp = pattern.split("1")
    
    if tmp[1] != "":
        answer = 1
    
    if tmp[0].count("!") % 2 == 1:
        answer = 0 if answer == 1 else 1
    
    print(answer)