def solution(date1, date2):
    answer = 0
    check = [date1[0] * (12 * 30) + date1[1] * 30 + date1[2], date2[0] * (12 * 30) + date2[1] * 30 + date2[2]]
    if check[0] < check[1]:
        answer = 1
        
    return answer