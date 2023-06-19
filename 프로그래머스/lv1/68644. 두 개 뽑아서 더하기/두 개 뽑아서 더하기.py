def solution(numbers):
    answer = []
    
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i]+numbers[j])
    
    answer.sort()                
    return answer