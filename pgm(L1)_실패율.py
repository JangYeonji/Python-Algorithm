#성공
def solution(N, stages):
    fail = {}
    for i in range(1,N+1):
        fail[i] = 0
    total = 0
    for i in range(N):
        try:
            total += stages.count(i)
            fail[i+1] = stages.count(i+1)/(len(stages)-total)
        except:
            fail[i+1] = 0
    result = dict(sorted(fail.items(), key=lambda x:-x[1]))
    return list(result.keys())