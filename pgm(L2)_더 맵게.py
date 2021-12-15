import heapq
def solution(scoville, K):
    answer = 0
    mix = 0
    
    heapq.heapify(scoville)
            
    while True:
        if len(scoville)<2:
            if scoville[0] >= K:
                break
            else:
                return -1
        mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        answer += 1
        heapq.heappush(scoville,mix)
        if scoville[0] >= K:
            break
    return answer