from collections import Counter
def solution(participant, completion):
    
    cnt = Counter(participant) - Counter(completion)
    
    return "".join(cnt)