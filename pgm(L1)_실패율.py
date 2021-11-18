#1차시도 실패. 1,6,7,9,13,23,24,25
def solution(N, stages):
    fail = {}
    for i in range(1,N+1):
        fail[i] = 0
    total = 0
    for i in range(N):
        total += stages.count(i)
        fail[i+1] = stages.count(i+1)/(len(stages)-total)
    result = dict(sorted(fail.items(), key=lambda x:-x[1]))
    return list(result.keys())