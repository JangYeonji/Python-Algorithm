import math
def solution(n):
    answer = 0

    if math.sqrt(n) % 1 == 0 :
        return (math.sqrt(n)+1) * (math.sqrt(n)+1) 
    else:
        return -1