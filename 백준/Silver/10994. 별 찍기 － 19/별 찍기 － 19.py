n = int(input())
cnt = 1

pattern = ["*"]

if n != 1:
    while cnt != n:
        cnt += 1
        for i in range(len(pattern)):
            pattern[i] = "* " + pattern[i] + " *"
        
        pattern = ["*" * len(pattern[0]), "*" + " " * (len(pattern[0]) - 2) + "*"] + pattern + ["*" + " " * (len(pattern[0]) - 2) + "*", "*" * len(pattern[0])]
        
print(*pattern, sep="\n")