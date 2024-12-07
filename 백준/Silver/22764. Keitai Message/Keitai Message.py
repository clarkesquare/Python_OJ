pattern = ["", ".,!? ", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
answer = ""
tmp = []

for _ in range(int(input())):
    answer = ""
    tmp = input().split("0")
    for i in tmp:
        if i != "":
            # answer += pattern[int(i[0])]
            answer += pattern[int(i[0])][(i.count(i[0]) - 1) % len(pattern[int(i[0])])]
    
    print(answer)