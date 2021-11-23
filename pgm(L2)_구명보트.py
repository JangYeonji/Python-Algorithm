def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    
    for idx,i in enumerate(people):
        if i <= limit//2 and idx==people[-1]:
            answer += 1
            break
        if i+people[-1] <= limit:
            answer+=1
            people.pop()
        else:
            answer+=1
            
    return answer