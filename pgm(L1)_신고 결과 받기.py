from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)

    report = set(report)
    
    left_report = defaultdict(set)
    right_report = defaultdict(int)
    
    stopID = []

    for r in report:
        r1, r2 = r.split()
        
        right_report[r2] += 1
        left_report[r1].add(r2)
        
        if right_report[r2] == k:
            stopID.append(r2)
            
    for s in stopID:
        for i in range(len(id_list)):
            if s in left_report[id_list[i]]:
                answer[i] += 1

    return answer


def solution(id_list, report, k):
    answer = []
    id_dict = {}
    id_dict2 = {}
    id_li = []
    report = set(report)
    
    for i in id_list:
        id_dict[i] = 0
        id_dict2[i] = 0
    
    #신고당한 유저
    for r in report:
        r1 = r.split()[1]
        id_dict[r1] += 1
        if id_dict[r1] >= k:
            id_li.append(r1)
            
    #신고한 유저 = 신고당한 유저
    for r in report:
        if r.split()[1] in id_li:
            id_dict2[r.split()[0]] += 1
    
    for i in id_dict2.values():
        answer.append(i)
        
    return answer