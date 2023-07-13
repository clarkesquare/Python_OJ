for i in range(int(input())):
    gap = 0
    scores = list(map(int, input().split()))
    scores = scores[1::]
    scores.sort(reverse=True)
    for j in range(len(scores)-1):
        if scores[j] - scores[j+1] > gap:
            gap = scores[j] - scores[j+1]
    
    print("Class", i+1)
    print(f"Max {max(scores)}, Min {min(scores)}, Largest gap {gap}")