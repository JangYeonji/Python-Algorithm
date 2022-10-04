def solution(skill, skill_trees):
    answer = 0

    skill = list(skill)
    
    for skill_ in skill_trees:
        tmp = True
        idx = 0
        for s_ in skill_:
            if s_ in skill:
                if s_ == skill[idx]:
                    idx += 1
                else:
                    tmp = False
                    continue
        if tmp:
            answer += 1
    
    return answer