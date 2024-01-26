votes = [0, 0, 0, 0] # Y, N, P, A

while True:
    vote = input()
    votes = [0, 0, 0, 0]
    if vote != '#':
        votes[0], votes[1], votes[2], votes[3] = vote.count('Y'), vote.count('N'), vote.count('P'), vote.count('A')
        if votes[3] / len(vote) >= 0.5:
            print('need quorum')
        elif votes[0] < votes[1]:
            print('no')
        elif votes[0] > votes[1]:
            print('yes')
        else:
            print('tie')
            
    else:
        break