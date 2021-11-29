#1차 시도. 2,5,18 실패.
def solution(priorities, location):
    q = []
    count = 0
    for idx, i in enumerate(priorities):
        q.append((idx,i))
    while q:
        tmp = q.pop(0)
        if tmp[1] < max(q ,key=lambda x:x[1])[1]:
            q.append(tmp)
        else:
            count += 1
            if tmp[0] == location:
                break
    return count