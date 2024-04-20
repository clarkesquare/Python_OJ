numbers = []
cnt = 0
temp = 0

for _ in range(int(input())):
    numbers = list(input().split())
    numbers[0] = int(numbers[0])
    cnt = 0
    temp = 0
    for i in range(1, numbers[0]+1):
        if numbers[i] == "X":
            temp += 1
        if i == numbers[0] or numbers[i] == "O":
            if cnt < temp:
                cnt = temp
            
            temp = 0
    
    print(f"The longest contiguous subsequence of X's is of length {cnt}")