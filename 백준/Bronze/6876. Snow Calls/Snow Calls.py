from string import ascii_uppercase

numbers = ["2", "3", "4", "5", "6", "7", "8", "9"]
alphabets = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
dials = ""
temp = ""
answer = []

for _ in range(int(input())):
    dials = input()
    temp = ""
    answer = []
    for i in dials:
        if i.isalpha():
            for j in range(len(alphabets)):
                if i in alphabets[j]:
                    temp += numbers[j]
                    break

        elif i != "-":
            temp += i
        
        if len(temp) >= 3:
            if len(answer) < 2:
                answer.append(temp)
                temp = ""
                
            else:
                if len(temp) == 4:
                    answer.append(temp)

    print(*answer, sep="-")