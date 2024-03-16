candidates = []
votes = []
i = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    i += 1
    candidates = []
    votes = []
    for _ in range(a):
        candidates.append(input())
        votes.append(0)
    
    for _ in range(b):
        x, y, z = input().split()
        votes[candidates.index(x)] += int(y)
    
    if votes.count(max(votes)) >= 2:
        print(f"VOTE {i}: THERE IS A DILEMMA")
    else:
        print(f"VOTE {i}: THE WINNER IS {candidates[votes.index(max(votes))]} {max(votes)}")