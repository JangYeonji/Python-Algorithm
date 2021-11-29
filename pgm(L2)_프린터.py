#while 문에서 만약 q에서 꺼낸 원소가 마지막이었을 경우를 고려

def solution(priorities, location):
    q = []
    count = 0
    for idx, i in enumerate(priorities):
        q.append((idx,i))
    while q:
        tmp = q.pop(0)
        if q==[]:
            count += 1
            break
        if tmp[1] < max(q ,key=lambda x:x[1])[1]:
            q.append(tmp)
        else:
            count += 1
            if tmp[0] == location:
                break
    return count