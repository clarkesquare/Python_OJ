n = int(input())
numbers = {"####.##.##.####": "0",
           "###..#####..###": "2",
           "###..####..####": "3",
           "#.##.####..#..#": "4",
           "####..###..####": "5",
           "####..####.####": "6",
           "###..#..#..#..#": "7",
           "####.#####.####": "8",
           "####.####..####": "9"}

tmp = input()
pattern = []
answer = ""
check = ""

for i in range(0, n, n//5):
    pattern.append(tmp[i:i+(n//5)])

i = -1
while i < (n//5) - 1:
    i += 1
    if i == (n//5)-1 and pattern[0][i] == "#" and pattern[1][i] == "#" and pattern[2][i] == "#" and pattern[3][i] == "#" and pattern[4][i] == "#":
        answer += "1"
        break
    
    if pattern[0][i] == "#" and pattern[1][i] == "#" and pattern[2][i] == "#" and pattern[3][i] == "#" and pattern[4][i] == "#" and (pattern[0][i+1] == "." and pattern[1][i+1] == "." and pattern[2][i+1] == "." and pattern[3][i+1] == "." and pattern[4][i+1] == "."):
        answer += "1"
        i += 1
    
    elif pattern[0][i] == "#" or pattern[1][i] == "#" or pattern[2][i] == "#" or pattern[3][i] == "#" or pattern[4][i] == "#":
        check = ""
        for j in range(5):
            check += pattern[j][i:i+3]
        
        answer += numbers[check]
        i += 2

print(answer)