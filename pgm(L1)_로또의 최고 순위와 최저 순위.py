def solution(lottos, win_nums):
    answer = [0,0]
    high = 0
    low = 0
    rank = {5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    for l in lottos:
        if l in win_nums:
            high += 1
            low += 1
        elif l == 0:
            high += 1
    
    if high >= 6:
        answer[0] = 1
    else:
        answer[0] = rank[high]
        
    if low >= 6:
        answer[1] = 1
    else:
        answer[1] = rank[low]
    
    return answer