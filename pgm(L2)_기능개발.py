#progresses = [99,99,99,99,99], speeds = [3,3,3,3,3] 테스트케이스
#2차시도 : 2 실패
def solution(progresses, speeds):
    queue = []
    finish = [] 
    
    for i in range(len(progresses)):
        queue.append((100-progresses[i])/speeds[i]) 
        finish.append((100-progresses[i])/speeds[i])
    
    for i in range(1, len(finish)):
        if finish[i-1]>finish[i]:
            finish[i] = finish[i-1]
            
    answer = [1] * len(set(finish))

    i=0
    while len(queue)>len(answer):
        if queue[i]>=queue[i+1]:
            answer[i] += 1
            queue.pop(i+1)
            i-=1
        i+=1
        
    return answer