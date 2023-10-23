for _ in range(int(input())):
    n = int(input())
    our_players = list(map(int, input().split()))
    scores = []
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        if a in our_players and b != -1 and not (b == 6 and c >= 1) and not b >= 7:
            scores.append([a, b, c])
    
    scores.sort(key=lambda x:(x[1], x[2]))
    print(scores[0][0], len(scores))