def solution(x):
    hsd = 0
    for i in range(len(str(x))):
        hsd += int(str(x)[i])
        
    if x % hsd == 0:
        return True
    else:
        return False