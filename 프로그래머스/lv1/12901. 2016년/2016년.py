def solution(a, b):
    answer = ''
    week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    day = (5 + sum(month[0:a-1]) + b-1) % 7
    answer = str(week[day])
    return answer