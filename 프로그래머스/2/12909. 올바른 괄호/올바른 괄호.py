def solution(s):
    if s[0] == "(":
        cnt = 0
        for i in s:
            if i == "(":
                cnt += 1

            else:
                if cnt >= 1:
                    cnt -= 1

                else:
                    cnt = -1
                    break
        
        if cnt == 0:
            return True
        
        else:
            return False
        
    else:
        return False