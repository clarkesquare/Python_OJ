def solution(before, after):
    answer = 0
    before = sorted(before)
    after = sorted(after)
    
    answer = 1 if before == after else 0
            
    return answer