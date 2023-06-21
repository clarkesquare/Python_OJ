def solution(cards1, cards2, goal):
    answer = ''
    
    while len(goal) != 0:
        if ((cards1[0] == goal[0]) if len(cards1) != 0 else 0) or ((cards2[0] == goal[0]) if len(cards2) != 0 else 0):
            if (cards1[0] == goal[0]) if len(cards1) != 0 else 0:
                del cards1[0]
            else:
                del cards2[0]
            del goal[0]
            answer = 'Yes'
        else:
            answer = 'No'
            break
            
    return answer