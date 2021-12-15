import heapq
def solution(operations):
    answer = []
    
    for i in operations:
        if i[0]=="I":
            heapq.heappush(answer,int(i[2:]))
        else:
            if answer!=[]:
                if i[2:]=="-1":
                    heapq.heappop(answer)
                else:
                    answer.pop()
                    
    if answer==[]:
        return [0,0]
    else:
        return [max(answer),min(answer)]