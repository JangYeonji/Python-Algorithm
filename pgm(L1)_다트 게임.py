def solution(dartResult):
    answer = 0
    score = []
    
    for idx, i in enumerate(dartResult):
        if i.isnumeric():
            score.append(int(i))
            if dartResult[idx-1]+dartResult[idx]=="10":
                score[-2] = 10
                score.pop()
        elif i.isalpha():
            if i=="S":
                score[-1] = score[-1] ** 1
            elif i=="D":
                score[-1] = score[-1] ** 2
            else:
                score[-1] = score[-1] ** 3
        else:
            if i=="*":
                if len(score)==1:
                    score[-1] = score[-1]*2
                else:
                    score[-1] = score[-1]*2
                    score[-2] = score[-2]*2
            elif i=="#":
                score[-1] = score[-1]*(-1)
    return sum(score)