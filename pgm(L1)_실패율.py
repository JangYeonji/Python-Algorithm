def solution(N, stages):
    answer = {}
    result = []

    l = len(stages)
    stages = sorted(stages)
    
    for i in range(1,N+1):
        answer[i] = 0
        if i in stages:
            answer[i] = stages.count(i) / (l - stages.index(i))

    for i in sorted(answer.items(), key=lambda x:-x[1]):
        result.append(i[0])
    return result