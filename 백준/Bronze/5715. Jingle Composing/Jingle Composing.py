pattern = []
answer = 0
temp = 0
identifier = ["W", "H", "Q", "E", "S", "T", "X"]
duration = [1, 1/2, 1/4, 1/8, 1/16, 1/32, 1/64]

while True:
    pattern = list(input().split("/"))
    if pattern != ["*"]:
        answer = 0
        for i in pattern:
            if i != "":
                temp = 0
                for j in i:
                    temp += duration[identifier.index(j)]
                
                if temp == 1:
                    answer += 1
            
        print(answer)

    else:
        break