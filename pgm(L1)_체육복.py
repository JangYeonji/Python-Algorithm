def solution(n, lost, reserve):
    answer = n - len(lost)
    reserve = sorted(reserve)
    lost = sorted(lost)
    
    for i in reserve:
        if i in lost:
            answer += 1
            lost[lost.index(i)] = 99
            reserve[reserve.index(i)] = 99
        elif i-1 in lost and i-1 not in reserve:
            answer += 1
            lost[lost.index(i-1)] = 99
            reserve[reserve.index(i)] = 99
        elif i+1 in lost and i+1 not in reserve:
            answer += 1
            lost[lost.index(i+1)] = 99
            reserve[reserve.index(i)] = 99
    
    return answer