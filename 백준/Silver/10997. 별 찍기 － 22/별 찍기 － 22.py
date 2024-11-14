n = int(input())

if n != 1:
    pattern = ["*****", "*    ", "* ***", "* * *", "* * *", "*   *", "*****"]
    tmp = 2
    while tmp != n:
        tmp += 1
        # 본체
        for i in range(len(pattern)):
            if i == 0:
                pattern[i] = "* " + pattern[i] + "**"
            
            else:
                pattern[i] = "* " + pattern[i] + " *"

        # 위아래
        pattern = ["*" * len(pattern[0]), "*" + " " * (len(pattern[0]) - 1)] + pattern + ["*" + " " * (len(pattern[0]) - 2) + "*", "*" * len(pattern[0])]

else:
    pattern = ["*"]
    
if len(pattern) != 1:
    pattern[1] = "*"

print(*pattern, sep="\n")