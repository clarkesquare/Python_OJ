pattern = []
temp = []
answer = []


for n in range(1, int(input()) + 1):
    pattern = []
    answer = []
    for _ in range(int(input())):
        pattern.append(input())
    
    for _ in range(int(input())):
        temp = list(input().split())
        for i in pattern:
            if i in temp:
                answer.append(i)
    
    print(f"Test set {n}:")
    for j in pattern:
        print(f"{j} is present" if j in answer else f"{j} is absent")
    
    print("")