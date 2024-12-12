from itertools import permutations

numbers = [["000000", "001100", "010010", "010010", "010010", "001100", "000000"], 
           ["000000", "000100", "001100", "000100", "000100", "000100", "000000"],
           ["000000", "011110", "000010", "011110", "010000", "011110", "000000"],
           ["000000", "011100", "000010", "000100", "000010", "011100", "000000"],
           ["000000", "000100", "001100", "010100", "111110", "000100", "000000"],
           ["000000", "011110", "010000", "011100", "000010", "010010", "001100"],
           ["000000", "010000", "010000", "011110", "010010", "011110", "000000"],
           ["000000", "011110", "000010", "000100", "000100", "000100", "000000"],
           ["000000", "011110", "010010", "011110", "010010", "011110", "000000"],
           ["011110", "010010", "010010", "011110", "000010", "000010", "000010"]]

pattern = []
tmp = []
tmp_number = ""
patterns = []
answer = [""] * 7
number = 0

for _ in range(7):
    pattern.append(input())

for j in range(0, len(pattern[0]), 6):
    tmp = []
    for i in range(7):
        tmp.append(pattern[i][j:j+6])
    
    tmp_number += str(numbers.index(tmp))

patterns = list(map("".join, permutations(sorted(tmp_number), len(tmp_number))))
if patterns[-1] != tmp_number:
    number = patterns[patterns.index(tmp_number) + 1]
    for j in number:
        j = int(j)
        for i in range(7):
            answer[i] += numbers[j][i]
    
    print(*answer, sep="\n")

else:
    print("The End")