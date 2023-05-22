import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    numer = denom1*numer2 + denom2*numer1
    denom = denom1 * denom2
    gcd = math.gcd(denom, numer)
    
    answer.append(numer//gcd)
    answer.append(denom//gcd)
    return answer